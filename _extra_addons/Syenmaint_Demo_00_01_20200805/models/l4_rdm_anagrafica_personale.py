# -*- coding: utf-8 -*-
import csv
from odoo import models, fields, exceptions, api, _
from datetime import timedelta

class l4_anagrafica_personale(models.Model):
    """  L4 - modello per la creazione delle anagrafiche del personale """
    _description = 'Anagrafica del Personale'
    _name = 'l4_rdm_anagrafica_personale'
    _rec_name = 'l4sm_descr'
    ##
    # codice del dipendente.
    l4sm_codice = fields.Char(string="Codice Dipendente", readonly=True, required=True, copy=False, default='New',
                              help="Codice progressivo del Dipendente")

    # Descrizione del dipendente
    l4sm_descr = fields.Char(string="Nome", help="Inserisci il nome del Dipendente")

    ##
    # riferimento dipendenti L4
    l4sm_dipendente_id = fields.Many2one(
        'hr.employee"', ondelete='restrict', string="L4 - Dipendenti", index=True,
        help="Inserisci il Dipendente di riferimento dell'L4")
    active = fields.Boolean('Active', default=True)

    @api.model
    def create(self, vals):
        """
        Alla creazione del treno per la definizione del codice progressivo sequenziale
        :param vals: valori del record
        :return: record creato
        """
        ##
        # definisco il codice
        if vals.get('l4sm_codice', 'New') == 'New':
            vals['l4sm_codice'] = self.env['ir.sequence'].next_by_code(
                'l4_rdm_anagrafica_personale_codice') or 'New'
        result = super(l4_anagrafica_personale, self).create(vals)
        return result
