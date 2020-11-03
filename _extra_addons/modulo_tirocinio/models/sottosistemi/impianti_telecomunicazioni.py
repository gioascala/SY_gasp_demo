from odoo import models, fields

class Impianti_telecomunicazioni(models.Model):
    _name = 'impianti_telecomunicazioni'

    unità_tecnologica=fields.Selection([("Reti Telematiche","Reti Telematiche"),("Tv","Tv"),("Tvcc","Tvcc"),("Diffusione Sonora","Diffusione Sonora"),("Videocitofonici","Videocitofonici"),("Citofonici","Citofonici"),("Telefonici","Telefonici")])
    elemento_tecnico = fields.Text()