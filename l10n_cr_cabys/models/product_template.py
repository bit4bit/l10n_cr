import logging
import requests
import datetime
import pytz
from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class ProductElectronic(models.Model):
    _inherit = "product.template"

    cabys_code = fields.Char(string="Código Cabys", required=True)

    # Funcion ejecutada al haber un cambio en el campo vat(cedula)
    @api.onchange('cabys_code')
    def onchange_cabys_code(self):

        endpoint = self.company_id.cabys_base_url
        now_utc = datetime.datetime.now(pytz.timezone('UTC'))
        now_cr = now_utc.astimezone(pytz.timezone('America/Costa_Rica'))
        date_cr = now_cr.strftime("%Y-%m-%dT%H:%M:%S-06:00")

        # Valida que existan el campo url_base
        if endpoint:
            endpoint = endpoint.strip()

            # Elimina la barra al final de la URL para prevenir error al conectarse
            if endpoint[-1:] == '/':
                endpoint = endpoint[:-1]

            headers = {
                'Authorization': 'Bearer {}'.format("GUWHwwVK2KQrRg=="),
            }

            data = {
                'cabys_desc': self.cabys_code,
            }

            try:
                # enviando solicitud post y guardando la respuesta como un objeto json
                response = requests.request(
                    "GET", endpoint, params=data, headers=headers)
                response_json = response.json()

                if 200 <= response.status_code <= 299:
                    ultimo_mensaje = 'Fecha/Hora: ' + str(date_cr) + ', Codigo: ' + str(
                        response.status_code) + ', Mensaje: ' + str(response_json.get('cabys_code'))

                    self.env.cr.execute("UPDATE res_company SET cabys_last_resp='%s' WHERE id=%s" % (
                        ultimo_mensaje, self.company_id.id))

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
