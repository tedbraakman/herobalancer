{
    'name': 'Herobalancer theme',
    'description': 'Herobalancer thema voor odoo.sh',
    'version': '1.0',
    'author': 'Chef R&D',
    'category': 'Theme/Creative',

    'depends': ['website', 'website_enterprise', 'web'],
    'data': [],
    'assets': {
        'web._assets_primary_variables': [
            'theme_herobalancer/static/scss/primary_variables.scss',

        ],
        'web._assets_backend_helpers': [
            'theme_herobalancer/static/scss/bootstrap_overridden.scss',
        ],
        'web.assets_backend': [
            'theme_herobalancer/static/scss/home_menu.scss'
        ],

    }
}