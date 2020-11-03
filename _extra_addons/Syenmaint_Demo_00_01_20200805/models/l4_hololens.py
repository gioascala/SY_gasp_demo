# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import os
import logging
import subprocess

_logger = logging.getLogger(__name__)

class l4_live_hololens(models.Model):
    """ L4 - Live Hololens """
    _name = 'syenmaint.l4_live_hololens'
    _rec_name = 'l4sm_codice_holo'

    l4sm_codice_holo = fields.Char(string="Codice", default='Live Hololens')
    syl4_title = fields.Char(string="Straming manutenzione", readonly=True, default="Straming Hololens 3D")