# -*- coding: utf-8 -*-

from odoo import models, fields, api

class l4_control_box_assets(models.Model):
    """ L4 - tabella che memorizza i riferimenti tra CB ed ASSETS """
    _name = 'syenmaint.l4_control_box_assets'

    l4sm_control_box_id = fields.Many2one(
        'syenmaint.l4_control_box', ondelete='set null', string="Control Box", index=True)
    l4sm_asset_id = fields.Many2one(
        'syenmaint.l4_assets', ondelete='set null', string="Asset", index=True)
