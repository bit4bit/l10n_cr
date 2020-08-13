# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools
from odoo.exceptions import UserError, Warning
from datetime import datetime, date, timedelta
import json
import requests
import re
import logging

_logger = logging.getLogger(__name__)


class res_company(models.Model):
    _name = 'res.company'
    _inherit = ['res.company']

    cabys_last_resp = fields.Text(string="Última Respuesta de API",
                                  help="Última Respuesta de API, esto permite depurar errores en caso de existir")

    cabys_base_url = fields.Char(string="URL Base", required=False,
                                 help="URL Base del END POINT", default="http://localhost/cabys/v1/cabys")

    def test_api(self):

        headers = {
            'Authorization': 'Bearer {}'.format("GUWHwwVK2KQrRg=="),
        }
        data = {
            'cabys_desc': 'almacenamiento',
        }

        endpoint = "http://localhost/cabys/v1/cabys"

        try:
            # enviando solicitud post y guardando la respuesta como un objeto json
            response = requests.request(
                "GET", endpoint, params=data, headers=headers)
            response_json = response.json()

            if 200 <= response.status_code <= 299:
                cabys_desc = response_json.get('cabys_desc')
                cabys_code = response_json.get('cabys_code')
                cabys_iva = response_json.get('cabys_iva')
                _logger.error('CABYS - OK.  INFO %s' % (cabys_desc))
            else:
                _logger.error('MAB - token_hacienda failed.  error: %s' %
                              (response.status_code))

        except requests.exceptions.RequestException as e:
            raise Warning(
                _('Error Obteniendo el Token desde MH. Excepcion %s' % (e)))
