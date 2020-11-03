# -*- coding: utf-8 -*-

from odoo import models, fields, api

class dpi(models.Model):
    """ Anagrafica Dispositivi di Protezione Individuali """
    _name = 'syenmaint.dpi'

    sm_name = fields.Char(string="Nome")
    sm_caratteristiche = fields.Char(string="Caratteristiche")
    sm_categoria = fields.Char(string="Categoria")
    sm_immagine = fields.Binary(string="Immagine")
    sm_tipologia = fields.Char(string="Tipologia")
    sm_frequenza = fields.Char(string="Frequenza")