from odoo import models, fields, api, _

class Impianti_climatizzazione(models.Model):
    _name = 'impianti_climatizzazione'

    unità_tecnologica=fields.Selection([("Condizionamento","Condizionamento"),("Riscaldamento","Riscaldamento")])
    elemento_tecnico = fields.Text()
