# -*- coding: utf-8 -*-

from odoo import models, fields, api

class control_box(models.Model):
    """ Anagrafica ControlBox """
    _name = 'syenmaint.control_box'

    sm_name = fields.Char(string="Nome")
    sm_stato = fields.Char(string="Stato")
    sm_denominazione = fields.Char(string="Denominazione")
    sm_rotabile = fields.Integer(string="Rotabile")
    sm_immagine = fields.Binary(string="Immagine")
