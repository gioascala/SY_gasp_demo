# -*- coding: utf-8 -*-
from odoo import api, fields, models
import logging
from datetime import timedelta
_logger = logging.getLogger(__name__)

class l4_piano_manutenzione_wizard(models.Model):
    """ L4 - Modello per in piano di manutenzione con wizard """
    _name = 'syenmaint.l4_piano_manutenzione_wizard'

    # recupero l'id della manutenzione
    man_id = fields.Many2one(
        'syenmaint.l4_manutenzione', 'Ordine di Manutenzione',
        index=True)
    l4sm_day_cyc = fields.Integer(string="Giorni Ciclo")
    # campo che definisce il numero dei cicli
    l4sm_num_cyc = fields.Integer(string="Numero cicli")
    # campo che indica che il piano di manutenzione è stato creato
    l4sm_piano_creato = fields.Boolean(string="Piano di manutenzione creato", readonly=True)

    def action_validate(self):
        """
        funzione che genera il piano di manutenzione in base alla manutenzione selezionata
        :return:
        """
        self.ensure_one()
        # vado a generare i figli in base al piano di manutenzione definito
        num_cyc = self.l4sm_num_cyc
        _logger.debug('Prova: {}'.format(self.man_id.l4sm_data_fabbisogno))
        if num_cyc > 0:
            # definisco la data di fabbisogno in base al piano
            data_fabbisogno_piano = self.man_id.l4sm_data_fabbisogno
            # recupero la manutenzione
            for c in range(num_cyc):
                data_fabbisogno_piano += timedelta(self.l4sm_day_cyc)
                self.env['syenmaint.l4_manutenzione'].create({
                    'l4sm_data_fabbisogno': data_fabbisogno_piano,
                    'l4sm_tipo_manutenzione_id': self.man_id.l4sm_tipo_manutenzione_id.id,
                    'l4sm_control_box_id': self.man_id.l4sm_control_box_id.id,
                    'l4sm_stato': 'p',
                })
        # setto il piano di manutenzione come creato!!!
        self.l4sm_piano_creato = True
        self.man_id.l4sm_piano_creato = True

