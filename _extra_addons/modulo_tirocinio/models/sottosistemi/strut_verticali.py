from odoo import models , fields

class Strutture_verticali(models.Model):
    _name='strutture_verticali'

    unità_tecnologica=fields.Selection([("Murature Portanti","Murature Portanti"),("Oassatura Portante","Oassatura Portante")])
    elemento_tecnico = fields.Text()