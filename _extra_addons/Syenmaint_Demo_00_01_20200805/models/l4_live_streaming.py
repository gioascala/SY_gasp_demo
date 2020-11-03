# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import os
import logging
from threading import Thread
import time
import subprocess
from subprocess import Popen


_logger = logging.getLogger(__name__)

class l4_live_streaming(models.Model):
    """ L4 - Live Streaming """
    _name = 'syenmaint.l4_live_streaming'
    _rec_name = 'l4sm_codice'

    l4sm_codice = fields.Char(string="Codice", default='Live Streaming')
    syl4_title = fields.Char(string="Straming Hololens 3D", readonly=True, default="Straming Manutenzione")
