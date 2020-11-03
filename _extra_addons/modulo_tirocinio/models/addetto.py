from odoo import models,fields,api,_
import datetime
import logging

_logger = logging.getLogger(__name__)

class Addetto_custom(models.Model):
    _name = 'addetto_custom'

    # name = fields.Char('Addetto', string='Addetto')
    syl4_manutenzione = fields.Many2one('manutenzione', ondelete='set null', string="Manutenzione", index=True)

    syl4_addetto = fields.Many2one('res.users', domain=lambda self: [("groups_id", '=', self.env['res.groups'].search([('full_name','=','Addetti')]).id )],string="Addetti",required=True)
    syl4_ore = fields.Float(string="Ore")

# class Addetto_custom_2(models.Model):
#     """ L4 - questo modello è per l'associazione delle ore calcolate con il dipendente """
#     _description = 'Personale ed Ore'
#     _name = 'addetto_custom_2'
#     _rec_name = 'l4sm_data_calcolo'
#     ##
#     l4sm_data_calcolo = fields.Char(string="Data Calcolo", help="Data del calcolo", readonly = True)
#     l4sm_inizio = fields.Char(string="Data di inizio", help="Data di inizio calcolo", readonly = True)
#     l4sm_fine = fields.Char(string="Data di Fine", help="Data di fine calcolo", readonly = True)
#     l4sm_tot_ore = fields.Char(string=" Totale Ore")
#
#     l4sm_id_addetto = fields.Char(string='ID Addetto')
