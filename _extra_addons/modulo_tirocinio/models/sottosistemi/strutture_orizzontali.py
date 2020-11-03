from odoo import models , fields , api , _

class Strutture_orizzontali(models.Model):
    _name='strutture_orizzontali'

    unità_tecnologica = fields.Selection([("Solai", "Solai"), ("Altro: Collegamenti verticali (scale)", "Altro: Collegamenti verticali (scale)")])
    elemento_tecnico = fields.Text()