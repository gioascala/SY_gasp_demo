from odoo import models, fields, api, _

class Impianti_sollevamento(models.Model):
    _name = 'impianti_sollevamento'

    unità_tecnologica=fields.Selection([("Ascensori e montacarichi","Ascensori e montacarichi"),("Scale Mobili e tapis roulant","Scale Mobili e tapis roulant")])
    elemento_tecnico = fields.Text()