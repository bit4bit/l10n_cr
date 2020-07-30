from odoo import models, fields


class ReferenceDocument(models.Model):
    _name = "reference.document"

    active = fields.Boolean(string="Active", required=False, default=True)
    code = fields.Char(string="Code", required=False, )
    name = fields.Char(string="Name", required=False, )
