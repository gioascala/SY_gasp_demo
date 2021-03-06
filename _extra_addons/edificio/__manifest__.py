# -*- coding: utf-8 -*-
{
    'name': "Edificio",

    'summary': """
        Gestione di un edificio storico""",

    'description': """
        Questo modulo serve per aiutare il nostro cliente a gestire al meglio
        un edificio di tipo storico, in particolare la sua manutenzione
    """,

    'author': "Alessandro Pio Budetti",
    'website': "None",
    

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Management',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/edificio.xml',
        'views/cronologia.xml',
        'security/edificio_access.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    
}
