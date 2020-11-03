# -*- coding: utf-8 -*-

from odoo import models, fields, api

class l4_tipo_manutenzione_misure(models.Model):
    """ L4 - tabella che memorizza i riferimenti tra tipologie di manutenzione e le misure da produrre """
    _name = 'syenmaint.l4_tipo_manutenzione_misure'

    l4sm_tipo_manutenzione_id = fields.Many2one(
        'syenmaint.l4_tipo_manutenzione', ondelete='set null', string="Tipo Manutenzione",
        index=True, oldname="l4sm_manutenzione_id")
    l4sm_misure_id = fields.Many2one(
        'syenmaint.l4_misure', ondelete='set null', string="Misura", index=True)
