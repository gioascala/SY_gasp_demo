# -*- coding: utf-8 -*-

from odoo import models, fields, api

class l4_task_routing(models.Model):
    """ Per la gestione dei task nei routing """
    _inherit = "mrp.routing.workcenter"

    task_manutenzione_ids = fields.Many2many('syenmaint.l4_task_manutenzione',
        string="Task da gestire")
