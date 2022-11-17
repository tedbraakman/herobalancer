{
    'name': 'Herobalancer theme',
    'description': 'Herobalancer thema voor odoo.sh',
    'version': '1.0',
    'author': 'Chef R&D',
    'category': 'Theme/Creative',

    'depends': ['website', 'website_enterprise', 'web'],
    'data': [
        'data/mail_templates.xml',
        ],
    'images': [
            'static/description/bookstore_screenshot.jpg',
    ],
    'assets': {
        'web._assets_primary_variables': [
            'theme_herobalancer/static/scss/primary_variables.scss',

        ],
        'web.assets_backend': [
            'theme_herobalancer/static/scss/bootstrap_overridden.scss',
            'theme_herobalancer/static/scss/home_menu.scss',
        ],

    }
}

# src/odoo/addons/mail/data/mail_templates.xml
#  - mail_notification_paynow
#  - mail_notification_ligh
#  - mail_notification_borders
#  - message_notification_email