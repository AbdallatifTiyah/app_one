{
    'name': "App One",
    'author': "Abdallatif Tiyah",
    'category': 'Tools',
    'version': '19.0.1.0',
    'license': 'LGPL-3',
    'depends': ['base',
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/property_view.xml',
        'views/owner_view.xml',
        'views/tag_view.xml'
    ],
    'application': True,
}