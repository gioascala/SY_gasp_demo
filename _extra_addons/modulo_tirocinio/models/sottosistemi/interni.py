from odoo import models, fields, api, _

class Interni(models.Model):
    _name = 'interni'

    unità_tecnologica = fields.Selection([("Partizioni fisse", "Partizioni fisse"), ("Partizioni smontabili", "Partizioni smontabili"),("Partizioni mobili", "Partizioni mobili"), ("Divisori e blocchi servizi", "Divisori e blocchi servizi"),("Porte e telai interni", "Porte e telai interni"), ("Finiture interne murarie", "Finiture interne murarie"), ("Finiture interne - pavimentazione", "Finiture interne - pavimentazione"), ("Soffittature", "Soffittature")])
    elemento_tecnico = fields.Text()