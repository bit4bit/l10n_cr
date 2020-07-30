from odoo import models, fields, api, _
from odoo.exceptions import UserError

class AccountInvoiceRefund(models.TransientModel):
    _inherit = "account.move.reversal"

    @api.model
    def _get_invoice_id(self):
        context = dict(self._context or {})
        active_id = context.get('active_id', False)
        if active_id:
            return active_id
        return ''

    reference_code_id = fields.Many2one(
        "reference.code", string="Code reference", required=True, )
    reference_document_id = fields.Many2one(
        "reference.document", string="Reference Document Id", required=True, )
    invoice_id = fields.Many2one(
        "account.move", string="Invoice Id", default=_get_invoice_id, required=False, )

    def reverse_moves(self):
        if self.env.user.company_id.frm_ws_ambiente == 'disabled':
            result = super(AccountInvoiceRefund, self).reverse_moves()
            return result
        else:
            moves = self.move_id or self.env['account.move'].browse(
                self._context['active_ids'])
            # Create default values.
            default_values_list = []
            for move in moves:
                if self.invoice_id.tipo_documento in ('FE', 'TE', 'FEE') and self.invoice_id.state_tributacion == 'rechazado':
                    tipo_doc = "NC"
                else:
                    tipo_doc = 'ND'

                default_values_list.append({
                    'ref': _('Reversal of: %s, %s') % (move.name, self.reason),
                    'date': self.date or move.date,
                    'invoice_date': move.is_invoice(include_receipts=True) and (self.date or move.date) or False,
                    'invoice_origin': self.invoice_id.sequence,
                    'journal_id': self.journal_id and self.journal_id.id or move.journal_id.id,
                    'invoice_id': self.invoice_id.id,
                    'tipo_documento': tipo_doc,
                    'reference_code_id': self.reference_code_id.code,
                    'reference_document_id': self.reference_document_id.code,
                })

            # Handle reverse method.
            if self.refund_method == 'cancel' or (moves and moves[0].type == 'entry'):
                new_moves = moves._reverse_moves(
                    default_values_list, cancel=False)
            elif self.refund_method == 'modify':
                new_moves = moves._reverse_moves(
                    default_values_list, cancel=False)
                moves_vals_list = []
                for move in moves.with_context(include_business_fields=True):
                    moves_vals_list.append(move.copy_data({
                        'invoice_payment_ref': move.name,
                        'date': self.date or move.date,
                    })[0])
                new_moves = moves.create(moves_vals_list)
            elif self.refund_method == 'refund':
                new_moves = moves._reverse_moves(default_values_list)
            else:
                return

            # Create action.
            action = {
                'name': _('Reverse Moves'),
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
                    'view_mode': 'tree',
                    'domain': [('id', 'in', new_moves.ids)],
                })
            return action