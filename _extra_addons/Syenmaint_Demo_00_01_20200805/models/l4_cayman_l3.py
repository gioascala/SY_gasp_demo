# -*- coding: utf-8 -*-
import csv
from odoo import models, fields, api, _  # , csv
import logging
import subprocess
import sys
from odoo.exceptions import AccessError, UserError
_logger = logging.getLogger(__name__)

class l4_cayman_l3(models.Model):
    """ L4 - Modello per la manutenzione da controlbox """
    _name = 'syenmaint.l4_cayman_l3'
    _rec_name = 'l4smcl3_codice'

    l4smcl3_codice = fields.Char(string="Codice", readonly=True, required=True, copy=False, default='New')
    # nome del cavo
    l4smcl3_name = fields.Char(string="Name")
    # cavi da produrre
    l4smcl3_total = fields.Integer(string="Total")
    # lotti da produrre (al messimo può essere = total)
    l4smcl3_batch = fields.Integer(string="Batch")
    # Lunghezza cavo
    l4smcl3_length = fields.Integer(string="Length")
    # Materia Prima
    l4smcl3_raw_material = fields.Char(string="Raw Material")
    # In Lavorazione
    l4smcl3_processing = fields.Char(string="Processing")

    @api.model
    def create(self, vals):
        """
        Alla creazione della riga di produzione definisco un codice progressivo e sequenziale
        :param vals:
        :return:
        """
        if vals.get('l4smcl3_codice', 'New') == 'New':
            vals['l4smcl3_codice'] = self.env['ir.sequence'].next_by_code(
                'syenmaint.l4_cayman_l3') or 'New'
        result = super(l4_cayman_l3, self).create(vals)
        return result

    # STRUTTURA FILE
    # 0 Checked;
    # 1 Name;
    # 2 Total;
    # 3 Batch;
    # 4 Length;
    # 5 Raw Material;
    # 6 Processing
    @api.multi
    def importaWireList(self):
        wire_list = ['Checked;Name;Total;Batch;Length;Raw Material;Processing;IDL4 \n']
        for record in self:
            # la stringa della riga del csv
            wire_list.append('1;{};{};{};{};{};{};{} \n'.format(
                record.l4smcl3_name,
                record.l4smcl3_total,
                record.l4smcl3_batch,
                record.l4smcl3_length,
                record.l4smcl3_raw_material,
                record.l4smcl3_processing,
                record.l4smcl3_codice))
        # scrivo il file
        fileWireList = open(r"C:\Users\Di Nardo Domenico\Documents\CLIENTI\syemnaint\CERPOWER\L3\DA_IMPORTARE\wire_list.csv", "w")
        fileWireList.writelines(wire_list)
        fileWireList.close()
        _logger.debug('file creato');
        #lancio l'import
        #subprocess.call([r'C:\Users\Di Nardo Domenico\Documents\CLIENTI\syemnaint\CERPOWER\L3\CaymanSam.exe', 'import'],
        #    stdout=subprocess.PIPE, shell=True)
        #subprocess.Popen([r'C:\Users\Di Nardo Domenico\Documents\CLIENTI\syemnaint\CERPOWER\L3\import_l3.bat'],
        #    shell=True)
        self.lanciaEsterno();
        #process = subprocess.Popen([r'C:\Users\Di Nardo Domenico\Documents\CLIENTI\syemnaint\CERPOWER\L3\import_l3.bat'],
        #    stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        #out, err = process.communicate()
        #_logger.debug('exe lanciato???');
        #if process.returncode not in [0, 1]:
        #    if process.returncode == -11:
        ##        message = _(
        #            'Wkhtmltopdf failed (error code: %s). Memory limit too low or maximum file number of subprocess reached. Message : %s')
        #    else:
        #        message = _('Wkhtmltopdf failed (error code: %s). Message: %s')
        #    raise UserError(message % (str(process.returncode), err[-1000:]))
        #else:
        #    if err:
        #        _logger.warning('wkhtmltopdf: %s' % err)
        #_logger.debug(subprocess.Popen('C:\\Windows\\System32\\notepad.exe'))
        #subprocess.call([r'C:\Users\Di Nardo Domenico\Documents\CLIENTI\syemnaint\CERPOWER\L3\import_l3.bat'])

    def lanciaEsterno(self):
        _logger.debug('eccoci')
        process = subprocess.Popen([r'C:\Users\Di Nardo Domenico\Documents\CLIENTI\syemnaint\CERPOWER\L3\import_l3.bat'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        codice = process.wait()
        _logger.warning(codice)
