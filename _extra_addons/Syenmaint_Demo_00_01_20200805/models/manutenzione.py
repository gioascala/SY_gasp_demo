# -*- coding: utf-8 -*-
import csv
from odoo import models, fields, api#, csv

class manutenzione(models.Model):
    """ Modello per la manutenzione da controlbox """
    _name = 'syenmaint.manutenzione'

    sm_name = fields.Char(string="Nome")
    sm_lat = fields.Float(string="Latitudine")
    sm_lng = fields.Float(string="Longitudine")
    sm_velocita = fields.Float(string="Velocità")
    sm_progressiva = fields.Char(string="descrizione")
    sm_riferimenti = fields.Char(string="Riferimenti")
    sm_tipo_tipoanomalia = fields.Many2one('syenmaint.tipo_evento_manutentivo',
        ondelete='set null', string="Tipologia", index=True)
    sm_rif_anomalia = fields.Char(string="Riferimento Anomalia")
    sm_id_control_box = fields.Char(string="Id ControlBox")
    sm_stato = fields.Integer(string="Stato")
    sm_stat = fields.Integer(string="Stat")
    sm_richiesta = fields.Integer(string="Richiesta")
    sm_valida = fields.Integer(string="Valida")
    sm_validato = fields.Boolean(string="Validato")
    sm_intervento_manutentivo_richiesto = fields.Integer(string="Intervento Manutentivo Richiesto")
    sm_scartato = fields.Boolean(string="Scartato")
    sm_kanban_state = fields.Char(string="Stato Kanban")
    sm_stato2 = fields.Integer(string="Stato 2")
    sm_stringa = fields.Char(string="Stringa")

    @api.multi
    def convalida(self):
        for record in self:
            record.sm_name = "convalidato"
            man_order = self.env['mrp.production'].create({
                #'name': 'WH/MO/000101',
                'name': self.env['ir.sequence'].next_by_code('mrp.production'),
                'product_id': 56,
                'product_uom_id': 1,
                'product_qty': 4,
                'bom_id': 10,
            })

    @api.multi
    def ripristina(self):
        for record in self:
            record.sm_name = "ripristinato"

    @api.multi
    def file_log(self):
        with open(r'C:\Users\Di Nardo Domenico\Documents\CLIENTI\syemnaint\grafici\logRFI\2019_08_1_19_29_33\ASS1.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            self.env['syenmaint.file_log'].search([('create_uid', '=', 2)]).unlink()
            for row in csv_reader:
                if row:
                    self.env['syenmaint.file_log'].create({'sm_time':row[0],
                          'sm_acc_x':row[1],
                          'sm_acc_y':row[2],
                          'sm_acc_z':row[3],
                          'sm_gyr_x':row[4],
                          'sm_gyr_y':row[5],
                          'sm_gyr_z':row[6],
                           })
        #apro la vista del grafico
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'syenmaint.file_log',
            'view_type': 'form',
            'view_mode': 'graph',
            'res_id': 'vista_grafico',
            'name': 'Log Manutenzione',
            #'domain': [('sm_time', '>', 8233842)],
        }



