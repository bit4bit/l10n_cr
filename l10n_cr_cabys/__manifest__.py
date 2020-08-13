{
    "name": "Cabys Costa Rica",
    "version": "13.0.0",
    "author": "TechMicro International Company S.A.",
    'license': 'LGPL-3',
    "website": "https://github.com/odoocr/l10n_cr",
    "category": "API",
    "summary": """Obtener Datos del Catálogo Cabys del BCCR-Ministerio Hacienda""",
    "description": """Obtiene automáticament los datos de Cabys para los productos""",
    "depends": ['base', 'cr_electronic_invoice'],
    "data": [
            'views/res_company_views.xml',
            'views/product_views.xml',
            # 'views/pos_templates.xml',
    ],
    # 'qweb': [
    #    'static/src/xml/actualizar_pos.xml',
    # ],
    "installable": True
}
