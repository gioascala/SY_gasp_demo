from odoo import models ,fields

class Distribuzione_energia_elettrica(models.Model):
    _name = 'distribuzione_energia_elettrica'

    unità_tecnologica= fields.Selection([("Cavi", "Cavi"), ("Apparecchi illuminanti", "Apparecchi illuminanti")])
    elemento_tecnico = fields.Text()