# -*- coding: utf-8 -*-

from odoo import models, fields, api


class l4_task_workorder(models.Model):
    """ Per la gestione dei task nei routing """
    _inherit = "mrp.workorder"

    #per tenere traccia dei task del routing
    task_routing_ids = fields.Many2many('syenmaint.l4_task_manutenzione',
        string="Task da gestire")

    task_routing_value = fields.Boolean(
        'Task eseguito?',
        help='Indicare se il task è stato eseguito o meno.')

    #per la creazione dell'ordine di lavoro
    @api.model
    def create(self, values):
        # Override della funzione originale
        record = super(l4_task_workorder, self).create(values)

