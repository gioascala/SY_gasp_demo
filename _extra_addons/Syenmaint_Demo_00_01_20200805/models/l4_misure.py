# -*- coding: utf-8 -*-

from odoo import models, fields, api

class l4_misure(models.Model):
    """ L4 - Anagrafica ControlBox """
    _name = 'syenmaint.l4_misure'
    _rec_name = 'l4sm_descr'

    l4sm_codice = fields.Char(string="Codice")
    l4sm_descr = fields.Char(string="Descrizione")
    l4sm_tipo = fields.Selection(string="Tipologia",
        selection=[('s', 'SI/NO'),  ('t', 'Testo'), ('o', 'Tempo'), ('n', 'Numero'), ('d', 'Data')])
    l4sm_uom_id = fields.Many2one(
        'uom.uom', ondelete='set null', string="UM", index=True)

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            record_name = record.l4sm_codice + ' - ' + record.l4sm_descr
            result.append((record.id, record_name))
        return result