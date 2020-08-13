from odoo import api, SUPERUSER_ID


def pre_init_hook(cr):
    from odoo.service import common
    from odoo.exceptions import Warning
    version_info = common.exp_version()
    server_serie = version_info.get('server_serie')
    if server_serie != '13.0':
        raise Warning(
            'Module supports Odoo series 13.0, found {}'.format(server_serie))
    return True


def post_init_hook(cr, registry):

    sequence_names = ['INV Secuencia', 'INV: Rectificación Secuencia',
                      'FACTURA Secuencia', 'FACTURA: Rectificación Secuencia',
                      'FECJ Secuencia', 'FEEJ Secuencia', 'NDJ Secuencia',
                      'TEJ Secuencia', 'TEJ: Rectificación Secuencia'
                      ]

    for sequence in sequence_names:
        _sql_sequence_inv = (
            """
            UPDATE ir_sequence SET implementation = 'no_gap', prefix = NULL, suffix = NULL,
            use_date_range = False, padding = 10, number_next = 1
            WHERE name = '"""+str(sequence)+"""'
        """
        )
        cr.execute(_sql_sequence_inv)
    
    journal_codes = ['FACTU', 'FECJ', 'FEEJ', 'NDJ', 'TEJ']
    for journal in journal_codes:
        _sql_journal_inv = (
            """
            UPDATE account_journal SET refund_sequence = False
            WHERE code = '"""+str(journal)+"""'
        """
        )
        cr.execute(_sql_journal_inv)
