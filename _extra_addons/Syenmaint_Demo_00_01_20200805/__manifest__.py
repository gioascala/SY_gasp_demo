# -*- coding: utf-8 -*-
{
    'name': "Syenmaint",

    'summary': """
        Modulo per la gestione della manutenzione""",

    'description': """
        Il modulo permette l'acquisizione delle informazioni dalla ControlBox
        Inoltre, permette la creazione degli ordini di manutenzione tramite la validazione
        degli eventi.
    """,

    'author': "Ing. Domenico Di Nardo",
    'website': "http://www.syenmaint.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # moduli dai quali dipende l'applicazione:
    # base per la gestione dei moduli
    # mrp per la produzione
    # board per la dashboard
    'depends': ['base','mrp', 'board'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/access.xml',
        'data/ir_sequence_data.xml',
        #'views/views.xml',
        #'views/data.xml',
        'views/anagrafiche.xml',
        #'views/templates.xml',
        #'views/syenmaint_board.xml',
        ##################################################################
        # L4SM
        ##################################################################
        'views/l4_menus.xml',
        'views/l4_control_box.xml',
        'views/l4_assiemi.xml',
        'views/l4_assets.xml',
        'views/l4_control_box_assets.xml',
        'views/l4_tipo_manutenzione.xml',
        'views/l4_misure.xml',
        'views/l4_assets_assiemi.xml',
        'views/l4_manutenzione.xml',
        'views/l4_task_manutenzione.xml',
        'views/l4_task_routing.xml',
        'views/l4_file_log.xml',
        'views/l4_log_container_file.xml',
        'views/l4_piano_manutenzione_wizard.xml',
        'views/l4_live_streaming.xml',
        'views/l4_hololens.xml',
        'views/l4_rdm_anagrafica_personale.xml',

        #'views/l4_task_workorder.xml',
        #################################################################
        # L4CL3
        #################################################################
        'views/l4_cayman_l3.xml',
    ],
    'qweb': ['static/src/xml/custom.xml',
             #'static/src/xml/tree_view_button.xml',
             ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
