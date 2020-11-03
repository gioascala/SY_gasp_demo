from odoo import models ,fields

class Guardiola(models.Model):
    _name = 'guardiola'

    unità_tecnologica = fields.Selection([("Controllo ingressi", "Controllo ingressi"), ("Energia elettrica", "Energia elettrica")])
    elemento_tecnico = fields.Text()