# -*- coding: utf-8 -*-

from odoo import models, fields, api

class l4_misure_manutenzione(models.Model):
    """ L4 - tabella che memorizza i riferimenti tra misure e manutenzione """
    _name = 'syenmaint.l4_misure_manutenzione'
    rec_name = 'l4sm_descr'
    l4sm_manutenzione_id = fields.Many2one(
        'syenmaint.l4_manutenzione', ondelete='set null', string="Manutenzione", index=True)
    l4sm_misure_id = fields.Many2one(
        'syenmaint.l4_misure', ondelete='set null', string="Misure", index=True)
    l4sm_valore = fields.Float(string="Valore", digits=(16,5))
    l4sm_descr = fields.Char(string="Misure - Manutenzione")

