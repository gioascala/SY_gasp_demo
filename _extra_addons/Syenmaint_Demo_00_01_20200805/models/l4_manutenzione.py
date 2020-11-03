# -*- coding: utf-8 -*-
import csv
from odoo import models, fields, exceptions, api, _#, csv
from datetime import timedelta
import logging
from odoo.exceptions import AccessError, UserError
_logger = logging.getLogger(__name__)

class l4_manutenzione(models.Model):
    """ L4 - Modello per la manutenzione da controlbox """
    _name = 'syenmaint.l4_manutenzione'
    _rec_name = 'l4sm_codice'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']
    l4sm_codice = fields.Char(string="Codice", readonly=True, required=True, copy=False, default='New')
    l4sm_data_fabbisogno = fields.Datetime(
        'Data Fabbisogno', copy=False, default=fields.Datetime.now,
        index=True, required=True)
    l4sm_tipo_manutenzione_id = fields.Many2one(
        'syenmaint.l4_tipo_manutenzione', ondelete='set null', string="Tipo Manutenzione", index=True)
    l4sm_control_box_id = fields.Many2one(
        'syenmaint.l4_control_box', ondelete='set null', string="Control Box", index=True)
    l4sm_stato = fields.Selection(string="Stato",
        selection=[('p', 'Proposto'), ('v', 'Validato'),
                   ('s', 'Scartato'), ('i', 'In Esecuzione'),
                   ('e', 'Eseguito'), ('r', 'Verificato')])
    l4sm_op_id = fields.Many2one(
        'mrp.production', ondelete='set null', string="Ordine di Manutenzione", index=True)
    l4sm_misure_manutenzione_ids = fields.One2many(
        'syenmaint.l4_misure_manutenzione', 'l4sm_manutenzione_id', 'Misure',
        copy=True)
    # campo note che indica lo stato dell'ordine di manutenzione
    l4sm_log_manutenzione = fields.Char(string="Log Manutenzione", readonly=True)
    # campo per la gestione del numero giorni ciclo
    l4sm_day_cyc = fields.Integer(string="Giorni Ciclo")
    # campo che definisce il numero dei cicli
    l4sm_num_cyc = fields.Integer(string="Numero cicli")
    # campo che indica che il piano di manutenzione è stato creato
    l4sm_piano_creato = fields.Boolean(string="Piano di manutenzione creato", readonly=True)

    @api.model
    def create(self, vals):
        """
        Alla creazione della manutenzione per la definizione del codice progressivo sequenziale
        :param vals:
        :return:
        """
        # se sono valorizzati i dati ciclo devo creare una manutenzione per ogni ciclo con un intervallo temporale
        # definito del numero giorni ciclo a partire dalla data di fabbisogno
        if vals.get('l4sm_codice', 'New') == 'New':
            vals['l4sm_codice'] = self.env['ir.sequence'].next_by_code(
                'syenmaint.l4_manutenzione') or 'New'
        result = super(l4_manutenzione, self).create(vals)
        return result

    @api.multi
    def pianifica_manutenzione_wiz(self):
        self.ensure_one()
        return {
            'name': _('Piano di Manutenzione Wizard'),
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'syenmaint.l4_piano_manutenzione_wizard',
            'view_id': self.env.ref('syenmaint.piano_manutenzione_wizard_form_view').id,
            'type': 'ir.actions.act_window',
            'context': {'default_man_id': self.id},
            'target': 'new',
        }


    @api.multi
    def pianifica_manutenzione(self):
        """
        funzione che genera il piano di manutenzione in base alla manutenzione selezionata
        :return:
        """
        # vado a generare i figli in base al piano di manutenzione definito
        num_cyc = self.l4sm_num_cyc
        if num_cyc > 0:
            # definisco la data di fabbisogno in base al piano
            data_fabbisogno_piano = self.l4sm_data_fabbisogno
            # recupero la manutenzione
            for c in range(num_cyc):
                data_fabbisogno_piano += timedelta(self.l4sm_day_cyc)
                self.env['syenmaint.l4_manutenzione'].create({
                    'l4sm_data_fabbisogno': data_fabbisogno_piano,
                    'l4sm_tipo_manutenzione_id': self.l4sm_tipo_manutenzione_id.id,
                    'l4sm_control_box_id': self.l4sm_control_box_id.id,
                    'l4sm_stato': 'p',
                })
        # setto il piano di manutenzione come creato!!!
        self.l4sm_piano_creato = True

    # override create per fare qualcosa dopo aver salvato la manutenzione
    @api.multi
    def write(self, values):
        return super(l4_manutenzione, self).write(values)

    @api.multi
    def convalida(self):
        for record in self:
            # elimino l'attività dalle notifiche
            self.env['mail.activity'].search([('res_id', '=', record.id)]).unlink()
            #Verifico se non è stata già gestita
            if record.l4sm_stato == "p":
                #recupero il tipo di manutenzione in gestione
                tipo_manutenzione_id = self.l4sm_tipo_manutenzione_id.id
                #recupero la distinta base in basi al tipo
                bom_id = self.env['syenmaint.l4_tipo_manutenzione'].browse(tipo_manutenzione_id).l4sm_codice_bom_id.id
                #Recupero l'articolo di riferimento
                product_id = self.env['mrp.bom'].browse(bom_id).product_id.id
                product_uom_id = self.env['mrp.bom'].browse(bom_id).product_uom_id.id
                #creo l'ordine
                man_order = self.env['mrp.production'].create({
                    'name': self.env['ir.sequence'].next_by_code('mrp.production'),
                    'product_id': product_id,
                    'product_uom_id': product_uom_id,
                    'product_qty': 1,
                    'bom_id': bom_id,
                })
                #Setto lo stato a v: validato e l'op appena creato
                record.l4sm_stato = "v"
                record.l4sm_op_id = man_order.id
                record.l4sm_log_manutenzione = 'Ordine di Manutenzione Creato!'

    @api.multi
    def scartata(self):
        for record in self:
            res = {}
            if record.l4sm_stato != "p":
                res['warning'] = {'title': _('Warning'), 'message': 'Errore'}
                return res
                # raise UserError(_('Evento manutentivo già gestito'))
            else:
                record.l4sm_stato = "s"

    @api.multi
    def verificata(self):
        for record in self:
            res = {}
            if record.l4sm_stato != "p":
                res['warning'] = {'title': _('Warning'), 'message': 'Errore'}
                return res
                # raise UserError(_('Evento manutentivo già gestito'))
            else:
                record.l4sm_stato = "r"

#Gestisco gli eventi di conferma ed avvio degli ordini di manutenzione dal modulo MRP
class l4_conferma_op(models.Model):
    _inherit = 'mrp.production'

    #faccio l'override dell'evento che crea gli ordini di lavoro
    @api.multi
    def button_plan(self):
        res = super(l4_conferma_op, self).button_plan()
        l4_man = self.env['syenmaint.l4_manutenzione'].search([('l4sm_op_id', '=', self.id)])
        l4_man.l4sm_stato = 'i'
        l4_man.l4sm_log_manutenzione = 'Ordine di Lavoro Creato!'

    #a chiusura dell'ordine di manutenzione
    @api.multi
    def button_mark_done(self):
        res = super(l4_conferma_op, self).button_mark_done()
        l4_man = self.env['syenmaint.l4_manutenzione'].search([('l4sm_op_id', '=', self.id)])
        l4_man.l4sm_stato = 'e' #eseguito
        l4_man.l4sm_log_manutenzione = 'Ordine di Manutenzione Completato!'
        _logger.debug('Prova: {}'.format(l4_man.l4sm_stato))

#Gestisco gli eventi degli ordini di lavoro
class l4_ordini_lavoro(models.Model):
    _inherit = 'mrp.workorder'

    #faccio l'override dell'evento che crea avvia la lavorazione
    @api.multi
    def button_start(self):
        res = super(l4_ordini_lavoro, self).button_start()
        l4_man = self.env['syenmaint.l4_manutenzione'].search([('l4sm_op_id', '=', self.production_id.id)])
        l4_man.l4sm_stato = 'i'
        l4_man.l4sm_log_manutenzione = 'Lavorazione [{}] avviata!'.format(self.name)

    #Per la messa in pausa della lavorazione
    @api.multi
    def button_pending(self):
        res = super(l4_ordini_lavoro, self).button_pending()
        l4_man = self.env['syenmaint.l4_manutenzione'].search([('l4sm_op_id', '=', self.production_id.id)])
        l4_man.l4sm_stato = 'i'
        l4_man.l4sm_log_manutenzione = 'Lavorazione [{}] in Pausa!'.format(self.name)

    #a chiusura della lavorazione
    @api.multi
    def record_production(self):
        res = super(l4_ordini_lavoro, self).record_production()
        l4_man = self.env['syenmaint.l4_manutenzione'].search([('l4sm_op_id', '=', self.production_id.id)])
        l4_man.l4sm_stato = 'i'
        l4_man.l4sm_log_manutenzione = 'Lavorazione [{}] Completata!'.format(self.name)
