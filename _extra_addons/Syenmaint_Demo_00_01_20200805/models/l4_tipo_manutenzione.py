# -*- coding: utf-8 -*-

from odoo import models, fields, api

class l4_tipo_manutenzione(models.Model):
    """ L4 - Anagrafica delle tipologie degli eventi manutentivi """
    _name = 'syenmaint.l4_tipo_manutenzione'
    _rec_name = 'l4sm_descrizione'

    l4sm_codice = fields.Char(string="Codice")
    l4sm_descrizione = fields.Char(string="Descrizione")
    l4sm_codice_bom_id = fields.Many2one('mrp.bom',
        ondelete='set null', string="Layout di manutenzione", index=True)
    l4sm_tipo_manutenzione_misure_ids = fields.One2many(
        'syenmaint.l4_tipo_manutenzione_misure', 'l4sm_tipo_manutenzione_id', 'Misure',
        copy=True, oldname="l4sm_tipo_manutenzione_ids")
    l4sm_video_rendering = fields.Binary(string="Video Rendering")
    file_name = fields.Char('File Name')