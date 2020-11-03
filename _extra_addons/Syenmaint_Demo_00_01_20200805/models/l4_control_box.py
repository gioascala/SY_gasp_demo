# -*- coding: utf-8 -*-

from odoo import models, fields, api

class l4_control_box(models.Model):
    """ L4 - Anagrafica ControlBox """
    _name = 'syenmaint.l4_control_box'
    _rec_name = 'l4sm_descr'

    l4sm_codice = fields.Char(string="Codice")
    l4sm_descr = fields.Char(string="Descrizione")
    l4sm_img = fields.Binary(string="Immagine")
    l4sm_product_id = fields.Many2one(
        'product.product', ondelete='set null', string="Control Box - Prodotto", index=True)
