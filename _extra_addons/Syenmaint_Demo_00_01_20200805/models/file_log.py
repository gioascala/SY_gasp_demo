# -*- coding: utf-8 -*-

from odoo import models, fields, api

class file_log(models.Model):
    """ Modello per la gestione dei file log per il diagramma """
    _name = 'syenmaint.file_log'

    sm_time = fields.Integer(string="Tempo")
    sm_acc_x = fields.Float(string="Accelezione X")
    sm_acc_y = fields.Float(string="Accelerazione Y")
    sm_acc_z = fields.Float(string="Accelezazione Z")
    sm_gyr_x = fields.Float(string="Giroscopia X")
    sm_gyr_y = fields.Float(string="Giroscopia Y")
    sm_gyr_z = fields.Float(string="Giroscopia Z")
    sm_tag_sb = fields.Char(string="Tag Sensor Box")
    sm_id_cb = fields.Many2one('syenmaint.control_box',
        ondelete='set null', string="Control Box", index=True)



