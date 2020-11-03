# -*- coding: utf-8 -*-

from odoo import models, fields, api

class l4_assets_assiemi(models.Model):
    """ L4 - tabella che memorizza i riferimenti tra ASSETS ed ASSIEMI """
    _name = 'syenmaint.l4_assets_assiemi'

    l4sm_asset = fields.Many2one(
        'syenmaint.l4_assets', ondelete='set null', string="Asset", index=True)
    l4sm_assieme = fields.Many2one(
        'syenmaint.l4_assiemi', ondelete='set null', string="Assieme", index=True)
