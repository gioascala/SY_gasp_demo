from odoo import models ,fields

class Fornitura_e_distribuzione_acqua(models.Model):
    _name='fornitura_e_distribuzione_acqua'

    unità_tecnologica = fields.Selection([("Sistema di irrigazione a sprinkler", "Sistema di irrigazione a sprinkler")])
    elemento_tecnico = fields.Text()