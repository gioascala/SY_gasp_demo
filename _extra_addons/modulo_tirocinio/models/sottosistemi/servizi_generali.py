from odoo import models ,fields

class Servizi_generali(models.Model):
    _name = 'servizi_generali'

    unità_tecnologica = fields.Selection([("Rimozione rifiuti", "Rimozione rifiuti"), ("Griglie di drenaggio", "Griglie di drenaggio"),("Zerbini e tappeti di ingresso", "Zerbini e tappeti di ingresso")])
    elemento_tecnico = fields.Text()