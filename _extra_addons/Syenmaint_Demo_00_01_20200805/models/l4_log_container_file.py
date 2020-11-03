# -*- coding: utf-8 -*-

from odoo import models, fields, api, modules
import logging
import csv
import os
import datetime

_logger = logging.getLogger(__name__)

class l4_log_container_file(models.Model):
    """ L4 - Schema di salvataggio dei file log/Report """
    _name = 'syenmaint.l4_log_container_file'
    _rec_name = 'l4sm_descr'

    l4sm_path = fields.Char(string="Percorso File", compute="sync_file_log")
    l4sm_descr = fields.Char(string="Descrizione File")
    l4sm_path_file = fields.Char(string="Percorso Completo del File")

    @api.depends('l4sm_path')
    def sync_file_log(self):
        """ funzione che permette di scandagliare la cartella path e recuperare i file """
        # base_path = os.path.dirname(modules.get_module_path('base'))
        # base_path = "C:\\cblog"
        base_path = "D:\\media\\SD\\log\\transponder\\2020\\02\\28"
        for d in os.listdir(base_path):
            file_id = self.env['syenmaint.l4_log_container_file'].create({
                    'l4sm_path': '{}\\{}'.format(base_path, d),
                    'l4sm_path_file': '{}\\{}'.format(base_path, d),
                    'l4sm_descr': d
                 })
            # _logger.debug('file: {}'.format(d))

    @api.multi
    def carica_log(self):
        # elimino tutto
        self.env['syenmaint.l4_log_container_dati'].search([('l4sm_BAU1', '>', 0)]).unlink()
        # seleziono i dati del file
        with open(self.l4sm_path_file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)
            next(csv_reader)
            for row in csv_reader:
                # scrivo i dati nella tabella
                if len(row) > 3:
                    _logger.debug('Prova: {}'.format(row[0]))
                    timestamp = datetime.datetime.fromtimestamp(float(row[0])/1000)
                    file_log_dati = self.env['syenmaint.l4_log_container_dati'].create({
                        'l4sm_time_date': timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                        'l4sm_BAU1': row[1],
                        'l4sm_BAU2': row[2],
                        'l4sm_IND1': row[3],
                        'l4sm_IND2': row[4],
                        'l4sm_ACC1X': row[5],
                        'l4sm_ACC1Y': row[6],
                        'l4sm_ACC1Z': row[7],
                        'l4sm_ACC2X': row[8],
                        'l4sm_ACC2Y': row[9],
                        'l4sm_ACC2Z': row[10],
                        'l4sm_USO': row[11],
                        'l4sm_OPT': row[12],
                        'l4sm_time_s': float(row[0])/1000,
                    })

class l4_log_container_dati(models.Model):
    """ L4 - tabella dati log """
    _name = 'syenmaint.l4_log_container_dati'

    l4sm_time_date = fields.Datetime(string="Tempo")
    l4sm_BAU1 = fields.Float(string="Spostamento X/SX")
    l4sm_BAU2 = fields.Float(string="Spostamento Z/SX")
    l4sm_IND1 = fields.Float(string="Spostamento Y/SX")
    l4sm_IND2 = fields.Float(string="Spostamento Y/DX")
    l4sm_ACC1X = fields.Float(string="Accelerazione X/SX")
    l4sm_ACC1Y = fields.Float(string="Accelerazione Y/SX")
    l4sm_ACC1Z = fields.Float(string="Accelerazione Z/SX")
    l4sm_ACC2X = fields.Float(string="Accelerazione X/DX")
    l4sm_ACC2Y = fields.Float(string="Accelerazione Y/DX")
    l4sm_ACC2Z = fields.Float(string="Accelerazione Z/DX")
    l4sm_USO = fields.Float(string="Distanza Cinghia Ultrasuoni")
    l4sm_OPT = fields.Float(string="Distanza Cinghia Ottico")
    l4sm_time_s = fields.Float(string="Tempo Secondi")