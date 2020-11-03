# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class l4_workorder_task(models.Model):
    """ L4 - Task da compilare in fase di manutenzione nella gestione dell'ordine di lavoro """
    _name = 'syenmaint.l4_workorder_task'

    l4sm_workorder_id = fields.Many2one(
        'mrp.workorder', 'Ordine di Mautenzione',
        index=True, ondelete='cascade', required=True)

    l4sm_task_id = fields.Many2one(
        'syenmaint.l4_task_manutenzione', 'Task')

    task_routing_value = fields.Boolean(
        'Task eseguito?',
        help='Indicare se il task è stato eseguito o meno.')


class l4_workorder_create_task(models.Model):
    """ Per la gestione dei task nei routing """
    _inherit = "mrp.production"

    # per la creazione dell'ordine di lavoro
    @api.multi
    def button_plan(self):
        # Override della funzione originale
        record = super(l4_workorder_create_task, self).button_plan()
        # appena l'ordine viene generato vado a creare la task list
        _logger.debug('IDW: {}'.format(self.id))
        # op_id = self.env['mrp.workorder'].browse(self.id)
        workorder = self.env['mrp.workorder'].search([('production_id', '=', self.id)])
        if workorder:
            for w in workorder:
                # recupero l'id dell'operazione
                operation_id = w.operation_id.id
                # recupero i task legati all'operation_id
                task_ids = self.env['mrp.routing.workcenter'].search([('id', '=', operation_id)])
                #for task_id in task_ids.task_manutenzione_ids:
                    # devo inserire un record in syenmaint_l4_workorder_task
                    #man_order = self.env['syenmaint.l4_workorder_task'].create({
                    #    'l4sm_workorder_id': 216,
                    #    'l4sm_task_id': task_id.id
                    #})
                    #_logger.debug('task_id: {}'.format(task_id.id))
