# -*- coding: utf-8 -*-
{
    'name': "modExt",

    'description': """
        Estende l'applicazione Edificio per farla diventare multi-user
    """,

    'author': "Alessandro Pio Budetti",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    # any module necessary for this one to work correctly
    'depends': ['edificio'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
