{
    'name': 'Herobalancer theme',
    'description': 'Herobalancer thema voor odoo.sh',
    'version': '1.0',
    'author': 'Chef R&D',
    'category': 'Theme/Creative',

    'depends': ['website', 'website_enterprise', 'web'],
    'data': [
        'views/assets.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            ('prepend', 'theme_herobalancer/static/scss/primary_variables.scss'),
            # 'theme_herobalancer/static/scss/primary_variables.scss',

        ],
    }
}