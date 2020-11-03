# -*- coding: utf-8 -*-
{
    'name': "moduloPdf",

    'summary': """
        Questo modulo è stato creato per collegare dipendenti e file PDF.""",

    'description': """
        None
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
        'documentiPDF.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable':True,
    'auto_install':False,
    'application':True,
    
}
