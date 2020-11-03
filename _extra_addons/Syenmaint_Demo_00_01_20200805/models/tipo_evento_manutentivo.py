# -*- coding: utf-8 -*-

from odoo import models, fields, api

class tipo_evento_manutentivo(models.Model):
    """ Anagrafica delle tipologie degli eventi manutentivi """
    _name = 'syenmaint.tipo_evento_manutentivo'
    _rec_name = 'sm_name'

    sm_name = fields.Char(string="Nome")
    sm_descrizione = fields.Char(string="Descrizione")
    sm_bom_id = fields.Many2one('mrp.bom',
        ondelete='set null', string="Layout di manutenzione", index=True)
