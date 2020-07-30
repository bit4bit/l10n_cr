from odoo import models, fields, api, _
from odoo.exceptions import UserError


class AccountDebitNote(models.TransientModel):
    _inherit = "account.debit.note"

    @api.model
    def _get_invoice_id(self):
        context = dict(self._context or {})
        active_id = context.get('active_id', False)
        if active_id:
            return active_id
        return ''

    reference_code_id = fields.Many2one(
        "reference.code", string="Reference Code", required=True, )
    reference_document_id = fields.Many2one(
        "reference.document", string="Reference Document", required=True, )
    invoice_id = fields.Many2one(
        "account.move", string="Invoice", default=_get_invoice_id, required=False, )

    def create_debit(self):
        self.ensure_one()
        if self.env.user.company_id.frm_ws_ambiente == 'disabled':
            result = super(AccountDebitNote, self).create_debit()
            return result
        else:
            new_moves = self.env['account.move']
            # Create default values.
            #default_values_list = []

            # copy sale/purchase links
            for move in self.move_ids.with_context(include_business_fields=True):
                # no podemos usar el prepare_default_values porque necesitamos customizarlo
                #default_values = self._prepare_default_values(move)

                if move.type in ('in_refund', 'out_refund'):
                    type = 'in_invoice' if move.type == 'in_refund' else 'out_invoice'
                else:
                    type = move.type

                default_values = {
                    'ref': '%s, %s' % (move.name, self.reason) if self.reason else move.name,
                    'date': self.date or move.date,
                    'invoice_date': move.is_invoice(include_receipts=True) and (self.date or move.date) or False,
                    'journal_id': self.journal_id and self.journal_id.id or move.journal_id.id,
                    'invoice_payment_term_id': None,
                    'debit_origin_id': move.id,
                    'invoice_origin': self.invoice_id.sequence,
                    'type': type,
                    'invoice_id': self.invoice_id.id,
                    'tipo_documento': 'ND',
                    'reference_code_id': self.reference_code_id.code,
                    'reference_document_id': self.reference_document_id.code,
                }

                if not self.copy_lines or move.type in [('in_refund', 'out_refund')]:
                    default_values['line_ids'] = [(5, 0, 0)]

                # Context key is used for l10n_latam_invoice_document for ar/cl/pe
                new_move = move.with_context(
                    internal_type='debit_note').copy(default=default_values)

                move_msg = _(
                    "This debit note was created from:") + " <a href=# data-oe-model=account.move data-oe-id=%d>%s</a>" % (
                        move.id, move.name)
                        
                new_move.message_post(body=move_msg)
                new_moves |= new_move

            action = {
                'name': _('Debit Notes'),
                'type': 'ir.actions.act_window',
                'res_model': 'account.move',
            }
            if len(new_moves) == 1:
                action.update({
                    'view_mode': 'form',
                    'res_id': new_moves.id,
                })
            else:
                action.update({
                    'view_mode': 'tree,form',
                    'domain': [('id', 'in', new_moves.ids)],
                })
            return action
