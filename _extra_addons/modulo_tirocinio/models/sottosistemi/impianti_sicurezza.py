from odoo import models, fields

class Impianti_sicurezza(models.Model):
    _name = 'impianti_sicurezza'

    unità_tecnologica=fields.Selection([("Antifurto ed Intrusione","Antifurto ed Intrusione"),("Antincendio","Antincendio")])
    elemento_tecnico = fields.Text()