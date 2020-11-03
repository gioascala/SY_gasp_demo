from odoo import models , fields

class Fondazioni(models.Model):
    _name='fondazioni'

    unità_tecnologica=fields.Selection([("Dirette ordinarie","Dirette ordinarie"),("Speciali","Speciali")])
    elemento_tecnico = fields.Text()