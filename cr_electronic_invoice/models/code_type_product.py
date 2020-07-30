import logging
from odoo import models, fields


_logger = logging.getLogger(__name__)


class CodeTypeProduct(models.Model):
    _name = "code.type.product"

    code = fields.Char(string="Code", required=False, )
    name = fields.Char(string="Name", required=False, )
