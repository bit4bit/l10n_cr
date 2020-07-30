{
    'name': 'Costa Rica Accounting Catalog',
    'url': 'https://github.com/odoocr/l10n_cr',
    'author': 'Odoo CR',
    'website': 'https://github.com/odoocr/l10n_cr',
    'category': 'Localization',
    'description': """
    Costa Rica Chart of Accounts
    Includes:
    ---------
    * account.account.template
    * account.tax.template
    * account.chart.template
    """,
    'depends': ['account'],
    'data': [
        'data/l10n_cr_chart.xml',
        'data/account.account.template.csv',
        'data/account_chart_template_data.xml',
        'data/account_tax_data.xml',
        'data/account_chart_template_configure_data.xml',
    ],
}
