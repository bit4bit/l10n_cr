from odoo import models, fields, api


class PaymentMethods(models.Model):
    """Add new payment methods to make it Miniterio de Hacienda
    Compliant"""
    _name = "payment.methods"

    active = fields.Boolean(string="Active", required=False, default=True)
    sequence = fields.Char(string="Sequence", required=False)
    name = fields.Char(string="Name", required=False)
    notes = fields.Text(string="Notes", required=False)


class AccountPaymentTerm(models.Model):
    _inherit = "account.payment.term"
    
    sale_conditions_id = fields.Many2one("sale.conditions", string="Condiciones de venta")
