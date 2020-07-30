import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class AccountJournalInherit(models.Model):
    """Add new fields to Journal class to make it Miniterio de Hacienda
    Compliant"""
    _name = 'account.journal'
    _inherit = 'account.journal'

    sucursal = fields.Integer(string="Branch", required=False, default="1")

    terminal = fields.Integer(string="Terminal", required=False, default="1")

    sequence_electronic_doc_confirmation = fields.Many2one(comodel_name="ir.sequence",
                                                           string="E-DOC Acceptance Sequence",
                                                           required=False)

    sequence_electronic_doc_partial_confirmation = fields.Many2one(comodel_name="ir.sequence",
                                                                   string="Partial E-DOC Acceptance"
                                                                   " sequence",
                                                                   required=False)

    sequence_electronic_doc_reject = fields.Many2one(comodel_name="ir.sequence",
                                                     string="E-DOC Rejection Sequence",
                                                     required=False)
