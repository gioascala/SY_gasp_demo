# -*- coding: utf-8 -*-
import csv
from odoo import models, fields, exceptions, api, _
from datetime import datetime, timedelta
import logging
import calendar
import werkzeug
import re

_logger = logging.getLogger(__name__)


class calcolo_ore(models.Model):

    _description = 'Calcolo delle Ore'
    _name = 'syenmaint_calcolo_ore'
    _rec_name = 'l4sm_codice'

    ##
    # codice del KPI
    l4sm_codice = fields.Char(string="Codice Coefficiente", default='CALCOLO_ORE', readonly=True, required=True, copy=False,
                              help="Inserisci il codice del coefficiente")

    ##
    # Seleziona modalitá
    l4sm_seleziona_modalita = fields.Selection([
        ('ma', 'Mese Anno'),
        ('dif', 'Data Inizio e Fine')],
        default='ma', required=True, string="Modalita Calcolo", help="Seleziona la modalita di calcolo delle ore", onchange="_scelta_anno")
    ##
    # mese
    l4sm_data_mese = fields.Selection([
        ('gen', 'Gennaio'),
        ('feb', 'Febbraio'),
        ('mar', 'Marzo'),
        ('apr', 'Aprile'),
        ('mag', 'Maggio'),
        ('giu', 'Giugno'),
        ('lug', 'Luglio'),
        ('ago', 'Agosto'),
        ('set', 'Settembre'),
        ('ott', 'Ottobre'),
        ('nov', 'Novembre'),
        ('dic', 'Dicembre')],
        string="Mese", help="Inserisci la Data di Riferimento della formula", )

    l4sm_data_anno = fields.Char(string="Anno", help="Inserisci la Data di Riferimento della formula")

    ##
    # data inizio periodo per il calcolo delle formule ad intervallo
    l4sm_data_inizio = fields.Datetime(string="Data Inizio", help="Inserisci la Data Inizio")

    # data fine periodo per il calcolo delle formule ad intervallo
    l4sm_data_fine = fields.Datetime(string="Data Fine", help="Inserisci la Data Fine")

    ##
    l4sm_modalita = fields.Selection([
        ('tu', 'Tutti'),
        ('man', 'Seleziona Dipendenti')],
        default='tu', required=True, string="Modalita Dipendenti", help="Seleziona la modalita di scelta dei dipendenti")

    l4sm_lista_addetti = fields.One2many(
        'addetto_custom','syl4_addetto', 'Personale ed Ore', force_save=True, required=True, store=True,
        help="Visualizzazione Calcolo Addetto / Ore ")

    # l4sm_lista_addetti_2 = fields.One2many(
    #     'addetto_custom_2', 'l4sm_id_addetto', 'Personaed Ore', force_save=True, required=True, store=True,
    #     help="Visualizzazione Calcolo Addetto / Ore ")

    l4sm_tot_ore = fields.Char(string=" Totale Ore")

    # data lavoro dipendente su cui fare il calcolo
    @api.model
    def create(self, vals):
        """
        Alla creazione della Cassa per la definizione del codice progressivo sequenziale
        :param vals: valori del record
        :return: record creato
        """
        ##
        if self.l4sm_seleziona_modalita != 'dif':
            if self.l4sm_data_anno:
                if len(self.l4sm_data_anno) != 4:
                    raise exceptions.Warning("ERRORE 42: L'anno deve essere lungo 4 caratteri ed essere numerico")
                var = re.sub("[^0-9]", "", self.l4sm_data_anno)
                if var == "":
                    var = "999"
                if int(var) < 1000 or int(var) > 9999:
                    raise exceptions.Warning("ERRORE 43: L'anno deve essere lungo 4 caratteri ed essere numerico")
        result = super(calcolo_ore, self).create(vals)
        return result

    @api.multi
    def write(self, vals):
        """
        override create per fare qualcosa dopo aver salvato la manutenzione
        :param values: valori legati all'intervento
        :return: intervento modificato
        """
        if self.l4sm_seleziona_modalita != 'dif':
            if vals.get("l4sm_data_anno"):
                if len(vals.get("l4sm_data_anno")) != 4:
                    raise exceptions.Warning("ERRORE 44: L'anno deve essere lungo 4 caratteri ed essere numerico")
                var = re.sub("[^0-9]", "", vals.get("l4sm_data_anno"))
                if var == "":
                    var = "999"
                if int(var) < 1000 or int(var) > 9999:
                    raise exceptions.Warning("ERRORE 45: L'anno deve essere lungo 4 caratteri ed essere numerico")
        result = super(calcolo_ore, self).write(vals)
        return result

    @api.onchange("l4sm_seleziona_modalita")
    def _scelta_anno(self):
        if self.l4sm_seleziona_modalita == 'ma':
            i = datetime.now()
            self.l4sm_data_anno = i.year

    @api.multi
    def calcola_ore(self):
        _logger.debug('ho chiamato calcolo ore')

        if self.l4sm_seleziona_modalita == 'dif':
            if self.l4sm_data_inizio < self.l4sm_data_fine:
                if self.l4sm_data_inizio:
                    inizio = self.l4sm_data_inizio
                if self.l4sm_data_fine:
                    fine = self.l4sm_data_fine
            else:
                raise exceptions.Warning("ERRORE 48: La data d'inizio deve essere precedente alla data di fine!")
        else:
            if self.l4sm_data_anno:
                if len(self.l4sm_data_anno) != 4:
                    raise exceptions.Warning("ERRORE 46: L'anno deve essere lungo 4 caratteri ed essere numerico")
                var = re.sub("[^0-9]", "", self.l4sm_data_anno)
                if var == "":
                    var = "999"
                if int(var) < 1000 or int(var) > 9999:
                    raise exceptions.Warning("ERRORE 47: L'anno deve essere lungo 4 caratteri ed essere numerico")
            switcher = {
                'gen': 1,
                'feb': 2,
                'mar': 3,
                'apr': 4,
                'mag': 5,
                'giu': 6,
                'lug': 7,
                'ago': 8,
                'set': 9,
                'ott': 10,
                'nov': 11,
                'dic': 12,
            }
            iniziofine = calendar.monthrange(int(self.l4sm_data_anno), switcher.get(self.l4sm_data_mese))
            # datetime(year, month, day, hour, minute, second, microsecond)
            inizio = datetime(int(self.l4sm_data_anno), switcher.get(self.l4sm_data_mese), 1)
            fine = datetime(int(self.l4sm_data_anno), switcher.get(self.l4sm_data_mese), iniziofine[1], 23, 59, 59)

        #Lista addetti (SET)
        list = self.env["addetto_custom"].search(
            ['&', ('syl4_manutenzione.data_manutenzione', '>=', str(inizio)),
             ('syl4_manutenzione.data_manutenzione', '<=', fine)])
        _logger.warning('lista addetti_manutenz')
        for elem in list:
            _logger.warning(elem)
        _logger.warning('\n')

        list_addetti = []
        for addetto_man in list:
            list_addetti.append(addetto_man.syl4_addetto.id)
        set_addetti_unique = set(list_addetti)

        nom = {}
        nom_srai = {}
        lista = []
        listadistampa = []
        dict_addetto_manutenzioni = {}

        _logger.warning('la lista ha dimensione { len(list)}')
        _logger.warning(len(list))
        _logger.warning('la lista UNIQUE ha dimensione { len(list)}')
        _logger.warning(len(set_addetti_unique))


        if self.l4sm_modalita == 'tu':
            _logger.warning('ho selezionato tu')
            if len(set_addetti_unique) != 0:
                somma_totale = 0
                for id_addetto in set_addetti_unique:
                    somma = 0
                    #lista.append(id_addetto.syl4_addetto) #??

                    pis = list.search(['&', ('syl4_addetto', '=', id_addetto), '&',
                                       ('syl4_manutenzione.data_manutenzione', '>=', str(inizio)),
                                       ('syl4_manutenzione.data_manutenzione', '<=', fine)])
                    for n in range(0, len(pis)):
                        somma += pis[n].syl4_ore
                    #nom[id_addetto] = somma
                    somma_totale += somma
                    _logger.warning(id_addetto)
                    _logger.warning(somma)

                    dict_addetto_manutenzioni[id_addetto] = somma
                    _logger.warning("L'addetto")
                    _logger.warning(id_addetto)
                    _logger.warning("Ha tatalizzato ore:")
                    _logger.warning(somma)
                    lista_manutenzioni_addetto = self.env["manutenzione"].search(
                        [('persone.syl4_addetto.id', '=', id_addetto )])
                    _logger.warning("\nLista manutenzioni di questo addetto:")
                    for man in lista_manutenzioni_addetto:
                        _logger.warning(man.descrizione_intervento)
                    _logger.warning("\n\n")

                self.l4sm_tot_ore = somma_totale
                _logger.warning(dict_addetto_manutenzioni)

        # valori = {'l4sm_data_calcolo': str(datetime.now() + timedelta(hours=2)).split('.')[0], 'l4sm_inizio': inizio,
        #           'l4sm_fine': fine}
        #
        # for k,v in dict_addetto_manutenzioni:
        #     valori = {'l4sm_data_calcolo': str(datetime.now() + timedelta(hours=2)).split('.')[0],
        #               'l4sm_inizio': inizio,
        #               'l4sm_fine': fine,
        #               'l4sm_tot_ore': v,
        #               'l4sm_id_addetto':k
        #               }
        #     self.l4sm_lista_addetti_2.create(valori)

                # for k,v in dict_addetto_manutenzioni:
                #     self.write()

            #     variabile = self.env["addetto_custom"].search([])
            #     for lo in range(0, len(variabile)):
            #         if variabile[lo] not in lista:
            #             listadistampa.append(variabile[lo].name)
            # if len(list) == 0:
            #     variabile = self.env["syenmaint.l4_rdm_anagrafica_personale"].search([])
            #     for lo in range(0, len(variabile)):
            #         listadistampa.append(variabile[lo].l4sm_descr)
        # else:
        #     if len(self.l4_rdm_personale_erp) != 0:
        #         if len(list) != 0:
        #             for addett in list:
        #                 somma = 0
        #                 if addett.l4sm_rdm_personale_id:
        #                     if addett.l4sm_rdm_personale_id in self.l4_rdm_personale_erp:
        #                         lista.append(addett.l4sm_rdm_personale_id)
        #                         if self.l4sm_data_dipendente:
        #                             pis = list.search(
        #                                 ['&', ('l4sm_rdm_personale_id', '=', addett.l4sm_rdm_personale_id.id), '&',
        #                                  ('l4sm_rdm_main_id.l4sm_odl_data_ora', '>=', str(inizio)),
        #                                  ('l4sm_rdm_main_id.l4sm_odl_data_ora', '<=', fine),
        #                                  ('l4sm_erp_personale_data', '=', self.l4sm_data_dipendente)])
        #                         else:
        #                             pis = list.search(
        #                                 ['&', ('l4sm_rdm_personale_id', '=', addett.l4sm_rdm_personale_id.id), '&',
        #                                  ('l4sm_rdm_main_id.l4sm_odl_data_ora', '>=', str(inizio)),
        #                                  ('l4sm_rdm_main_id.l4sm_odl_data_ora', '<=', fine)])
        #                         for n in range(0, len(pis)):
        #                             somma += pis[n].l4sm_erp_personale_ore
        #                             listasrai.append(pis[n].l4sm_rdm_main_id["l4sm_erp_srai"])
        #                             nom[addett.l4sm_rdm_personale_id.l4sm_descr] = somma
        #                             nom_srai[addett.l4sm_rdm_personale_id.l4sm_descr] = listasrai
        #                 listasrai = []
        #             # _logger.warning(nom)
        #             # _logger.warning(nom_srai)
        #
        #             for lo in range(0, len(self.l4_rdm_personale_erp)):
        #                 if self.l4_rdm_personale_erp[lo] not in lista:
        #                     listadistampa.append(self.l4_rdm_personale_erp[lo].l4sm_descr)
        #         if len(list) == 0:
        #             for lo in range(0, len(self.l4_rdm_personale_erp)):
        #                 listadistampa.append(self.l4_rdm_personale_erp[lo].l4sm_descr)
        # stamp = []
        # for io in nom.items():
        #     stamp.append(io)
        # valori = {'l4sm_data_calcolo': str(datetime.now() + timedelta(hours=2)).split('.')[0], 'l4sm_inizio': inizio,
        #           'l4sm_fine': fine}
        # ok = self.env['syenmaint.l4_personale_ore2'].create(valori)
        # record_ids = self.env["syenmaint.l4_personale_ore2"].search([('id', '=', ok.id)])
        # record_this = self.env["syenmaint.l4calcolo"].search([('id', '=', self.id)])
        # # _logger.warning(record_ids)
        # somma = 0
        # if len(self.l4sm_lista_addetti) != 0:
        #     for recorde in record_this:
        #         for ido in self.l4sm_lista_addetti:
        #             recorde.write({
        #                 'l4sm_lista_addetti': [(2, ido.id)]
        #             })
        # for record in record_ids:
        #     for recorde in record_this:
        #         for io in nom.items():
        #             somma += io[1]
        #             # _logger.warning(nom_srai.get(io[0]))
        #             record.write({
        #                 'l4sm_lista_addetti': [(0, 0, {'l4sm_personale': io[0], 'l4sm_ore': io[1],
        #                                                'l4sm_srai_lavori': nom_srai.get(io[0])})]
        #             })
        #             recorde.write({
        #                 'l4sm_lista_addetti': [(0, 0, {'l4sm_personale': io[0], 'l4sm_ore': io[1],
        #                                                'l4sm_srai_lavori': nom_srai.get(io[0])})]
        #             })
        #         for la in listadistampa:
        #             # _logger.warning(la)
        #             record.write({
        #                 'l4sm_lista_addetti': [(0, 0, {'l4sm_personale': la, 'l4sm_ore': 0, 'l4sm_srai_lavori': 0})]
        #             })
        #             recorde.write({
        #                 'l4sm_lista_addetti': [(0, 0, {'l4sm_personale': la, 'l4sm_ore': 0, 'l4sm_srai_lavori': 0})]
        #             })
        #         record.write({'l4sm_tot_ore': somma})
        #         recorde.write({'l4sm_tot_ore': somma})
        # stamp = ''
        # for io in nom.items():
        #     stamp += '' + str(io) + '\n'
        #     _logger.warning(stamp)
        # raise exceptions.Warning(stamp)
        # return {
        #     'name': str(datetime.now()).split('.')[0],
        #     'view_type': 'form',
        #     'view_mode': 'form',
        #     'res_model': 'syenmaint.l4_personale_ore2',
        #     'type': 'ir.actions.act_window',
        #     'target': 'current',
        #     }