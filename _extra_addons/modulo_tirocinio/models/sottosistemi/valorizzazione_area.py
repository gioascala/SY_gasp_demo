from odoo import models ,fields

class Valorizzazione_area(models.Model):
    _name = 'valorizzazione_area'

    unità_tecnologica = fields.Selection([("Campo da calcio", "Campo da calcio"), ("Campo da basket", "Campo da basket"),("Campo da tennis asfaltati o in cemento", "Campo da tennis asfaltati o in cemento")])
    elemento_tecnico = fields.Text()