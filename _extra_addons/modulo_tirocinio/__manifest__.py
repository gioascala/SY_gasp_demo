# -*- coding: utf-8 -*-
{
    'name': "Gestione edifici",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/edificio.xml',
        'sequences/sequenza_edifici.xml',
        'sequences/sequenza_rilevazioni.xml',
        'views/rilevazioni.xml',
        'views/rilevazioni_sensore.xml',
        'views/foto.xml',
        'security/utenti.xml',
        'views/manutenzione.xml',
        'mail/mail_template.xml',
        'mail/invio_mail.xml',

        'views/sottosistemi/aree_di_parcheggio.xml',
        'views/sottosistemi/climatizzazione.xml',
        'views/sottosistemi/distr_energia_elettrica.xml',
        'views/sottosistemi/fondazioni.xml',
        'views/sottosistemi/fornitura_acqua.xml',
        'views/sottosistemi/gas.xml',
        'views/sottosistemi/guardiola.xml',
        'views/sottosistemi/idrici_sanitari.xml',
        'views/sottosistemi/impianti_elettrici.xml',
        'views/sottosistemi/interni.xml',
        'views/sottosistemi/segnaletica.xml',
        'views/sottosistemi/servizi_generali.xml',
        'views/sottosistemi/sicurezza.xml',
        'views/sottosistemi/sollevamento.xml',
        'views/sottosistemi/strutture_verticali.xml',
        'views/sottosistemi/strutture_orizzontali.xml',
        'views/sottosistemi/telecomunicazioni.xml',
        'views/sottosistemi/valorizzazione_area.xml',
        'views/sottosistemi/verde_esterno.xml',
        'views/sottosistemi/verso_esterno.xml',
        'views/sottosistemi/zone_pedonali_esterna.xml',

        'views/guasti/coperture.xml',
        'views/guasti/finiture_interne.xml',
        'views/guasti/fondazioni.xml',
        'views/guasti/infissi_esterni.xml',
        'views/guasti/muri_esterni.xml',
        'views/guasti/partizioni_fisse.xml',
        'views/guasti/pavimentazioni.xml',
        'views/guasti/strutture_orizzontali.xml',
        'views/guasti/strutture_verticali.xml',
        'views/guasti.xml',
        'views/addetto.xml',
        'views/calcolo_ore.xml',


    ],
    # only loaded in demonstration mode
    'demo': [
                'demo.xml',
    ],
}
