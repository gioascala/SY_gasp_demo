from odoo import models ,fields

class Verde_esterno(models.Model):
    _name='verde_esterno'

    unità_tecnologica = fields.Selection([("Prati", "Prati"), ("Alberi a foglia caduca", "Alberi a foglia caduca"), ("Sempreverdi", "Sempreverdi"),("Cespugli", "Cespugli"), ("Siepi", "Siepi"), ("Aiuole fiorite", "Aiuole fiorite")])
    elemento_tecnico = fields.Text()