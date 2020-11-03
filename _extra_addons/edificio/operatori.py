from odoo import models, fields

class Operatori(models.Model):
    _name= 'edificio.operatori'
    _description = 'Operatori coinvolti nella manutenzione'

    name= fields.Char(string='Scheda n°:', required=True)
    edificio_id = fields.Many2many('edificio.edificio',string='Edificio',required=True)
    operatore1_id = fields.Many2one("res.partner",string='Facility manager', required=True)
    operatore2_id = fields.Many2one("res.partner",string='Committente', required=True)
    operatore3_id = fields.Many2one("res.partner",string='Fornitore della manutenzione', required=True)
    operatore4_id = fields.Many2one("res.partner",string='Proprietario', required=True)

