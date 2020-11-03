from odoo import models ,fields

class Segnaletica_e_cartelli_esterni(models.Model):
    _name='segnaletica_e_cartelli_esterni'

    unità_tecnologica = fields.Selection([("Barre di accesso / posizionamento segnaletica/ integrità","Barre di accesso / posizionamento segnaletica/ integrità")])
    elemento_tecnico = fields.Text()