from odoo import models , fields , api , _

class Fondazioni(models.Model):
    _name='g_fondazioni'

    elemento_tecnico=fields.Text()
    tipo_di_guasto=fields.Text()
    possibili_cause=fields.Text(string="Possibili cause di guasto")
    segnali_deboli=fields.Text(string="Segnali di deterioramento (segnali Deboli) ")