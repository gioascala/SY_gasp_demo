from odoo import models , fields

class Impianti_idrici_sanitari(models.Model):
    _name='impianti_idrici_sanitari'

    unità_tecnologica=fields.Selection([("Adduzione Idrica","Adduzione Idrica"),("Distribuzione Idrica","Distribuzione Idrica"),("Smaltimento Idrico","Smaltimento Idrico")])
    elemento_tecnico = fields.Text()