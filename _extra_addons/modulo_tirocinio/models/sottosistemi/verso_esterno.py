from odoo import models ,fields

class Verso_esterno(models.Model):
    _name='verso_esterno'

    unità_tecnologica = fields.Selection([("Muri esterni", "Muri esterni"), ("Griglie e schermature esterne", "Griglie e schermature esterne"),("Parapetti e ringhiere", "Parapetti e ringhiere"), ("Infissi esterni", "Infissi esterni"),("Porte esterne", "Porte esterne"), ("Coperture", "Coperture")])
    elemento_tecnico = fields.Text()