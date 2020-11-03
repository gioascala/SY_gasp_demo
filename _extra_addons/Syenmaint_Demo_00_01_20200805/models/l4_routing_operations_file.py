# -*- coding: utf-8 -*-

from odoo import models, fields, api

class l4_routing_operations_file(models.Model):
    _inherit = 'mrp.workorder'

    l4sm_video_operation = fields.Binary(string="Video Operazione")
    file_name = fields.Char('File Name')