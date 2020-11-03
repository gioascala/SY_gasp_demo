# -*- coding: utf-8 -*-

from odoo import models, fields, api

class l4_task_manutenzione(models.Model):
    """ L4 - Task da compilare in fase di manutenzione """
    _name = 'syenmaint.l4_task_manutenzione'
    _rec_name = 'l4sm_descr'

    l4sm_codice = fields.Char(string="Codice", readonly=True, required=True, copy=False, default='New')
    l4sm_descr = fields.Char(string="Descrizione")

    @api.model
    def create(self, vals):
        """
        Alla creazione del task per definire un codice progressivo
        :param vals:
        :return:
        """
        if vals.get('l4sm_codice', 'New') == 'New':
            vals['l4sm_codice'] = self.env['ir.sequence'].next_by_code(
                'syenmaint.l4_task_manutenzione') or 'New'
        result = super(l4_task_manutenzione, self).create(vals)
        return result
