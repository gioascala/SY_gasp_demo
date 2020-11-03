from odoo import models, fields, api, _
from . import connettore
import datetime
import base64
import pytz


class Edificio(models.Model):
    _name = 'edificio'
    _rec_name = 'nome_edificio'

    id_edificio = fields.Char(string="Id Edificio", readonly=True, default=lambda self: _('New'))
    nome_edificio = fields.Text(required=True)
    indirizzo_edificio = fields.Text(required=True)
    syl4_immagine_edificio = fields.Binary('Immagine edificio', attachment=True,  store=True)
    cartelladocuments = fields.Many2one('muk_dms.directory',string="Directory File")

    aree_di_parcheggio = fields.Many2many('aree_di_parcheggio')
    distribuzione_energia_elettrica = fields.Many2many('distribuzione_energia_elettrica')
    fondazioni = fields.Many2many('fondazioni')
    fornitura_e_distribuzione_acqua = fields.Many2many('fornitura_e_distribuzione_acqua',
                                                       string="Fornitura e distribuzione dell'acqua")
    guardiola = fields.Many2many('guardiola')
    impianti_climatizzazione = fields.Many2many('impianti_climatizzazione', string="Impianti di climatizzazione")
    impianti_elettrici = fields.Many2many('impianti_elettrici')
    impianti_gas = fields.Many2many('impianti_gas')
    impianti_idrici_sanitari = fields.Many2many('impianti_idrici_sanitari')
    impianti_sicurezza = fields.Many2many('impianti_sicurezza')
    impianti_sollevamento = fields.Many2many('impianti_sollevamento')
    impianti_telecomunicazioni = fields.Many2many('impianti_telecomunicazioni')
    interni = fields.Many2many('interni')
    segnaletica_e_cartelli_esterni = fields.Many2many('segnaletica_e_cartelli_esterni')
    servizi_generali = fields.Many2many('servizi_generali')
    strut_verticali = fields.Many2many('strutture_verticali', string="Strutture verticali")
    strutture_orizzontali = fields.Many2many('strutture_orizzontali')
    valorizzazione_area = fields.Many2many('valorizzazione_area', string="Valorizzazione dell'area")
    verde_esterno = fields.Many2many('verde_esterno')
    verso_esterno = fields.Many2many('verso_esterno')
    zona_pedonali_esterne = fields.Many2many('zona_pedonali_esterne')

    @api.model
    def create(self, vals):
        if vals.get('id_edificio', _('New')) == _('New'):
            vals['id_edificio'] = self.env['ir.sequence'].next_by_code('edificio.sequenza') or _('New')
        result = super(Edificio, self).create(vals)
        return result

    def lettura_rilevazione(self, lista_rilevazioni):
        lista_rilevazioni = self.lettura_rilevazione_sensore(lista_rilevazioni)
        lista_rilevazioni_sensore = self.lettura_rilevazione_sensore(lista_rilevazioni)
        lista_rilevazioni2 = lista_rilevazioni.copy()

        for rilevazione in lista_rilevazioni:
            lista_rilevazioni2.remove(rilevazione)
            for rilevazione2 in lista_rilevazioni2:
                if (abs(rilevazione2['timestamp'] - rilevazione['timestamp'])) <= datetime.timedelta(minutes=1):
                    lista_rilevazioni.remove(rilevazione2)

        for rilevazione in lista_rilevazioni:
            del rilevazione["valore"]
            del rilevazione["id_sensore"]
            del rilevazione["tipo_sensore"]
            self.env['rilevazione'].create(rilevazione)

        for rilevazione_sensore in lista_rilevazioni_sensore:
            for rilevazione in lista_rilevazioni:
                if abs(rilevazione["timestamp"] - rilevazione_sensore["timestamp"]) <= datetime.timedelta(seconds=60):
                    rilevazione_sensore["id_rilevazione"] = rilevazione["id_rilevazione"]

        for rilevazione_sensore in lista_rilevazioni_sensore:
            del rilevazione_sensore["timestamp"]
            del rilevazione_sensore["id_edificio"]
            self.env['rilevazione_sensore'].create(rilevazione_sensore)

    def lettura_rilevazione_sensore(self, lista_rilevazioni):
        lista_rilevazioni2 = lista_rilevazioni.copy()
        lista_rilevazioni_sensore = []

        for rilevazione in lista_rilevazioni:
            lista_rilevazioni2.remove(rilevazione)
            i = 2
            media = rilevazione["valore"]
            dizionario = rilevazione.copy()
            for rilevazione2 in lista_rilevazioni2:
                if rilevazione2['id_sensore'] == rilevazione['id_sensore'] and (
                abs(rilevazione2['timestamp'] - rilevazione['timestamp'])) <= datetime.timedelta(seconds=2):
                    media = (media * (i - 1) + rilevazione2['valore']) / i
                    i = i + 1
                    dizionario["valore"] = media
                    lista_rilevazioni.remove(rilevazione2)

            lista_rilevazioni_sensore.append(dizionario)

        return lista_rilevazioni_sensore

    def letturaDB(self):
        collection = connettore.connessione()
        lista_rilevazioni = []
        lista_rilevazioni2 = []

        for rilevazione in collection.find(
                {"id_edificio": self.id_edificio, "lettura": False, "id_sensore": {'$exists': True}},
                {"_id": False, "lettura": False}):
            rilevazione['id_rilevazione'] = _('New')
            rilevazione['timestamp'] = (rilevazione.get("timestamp").as_datetime()).replace(tzinfo=None)
            lista_rilevazioni.append(rilevazione)
            lista_rilevazioni2.append(rilevazione.copy())
        collection.update_many({"id_edificio": self.id_edificio, "id_sensore": {'$exists': True}, "lettura": False},
                               {'$set': {"lettura": True}})
        self.lettura_rilevazione(lista_rilevazioni)

        return {
            'name': _('Rilevazioni'),
            'domain': [('id_edificio', '=', self.id_edificio)],
            'view_type': 'form',
            'res_model': 'rilevazione',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def lettura_img(self):
        collection = connettore.connessione()
        for foto in collection.find({"id_edificio": self.id_edificio, "posizione": {'$exists': True},
                                     "lettura": False}, {"_id": False, "lettura": False}):
            foto['image'] = base64.encodebytes(foto["image"])
            if self.env.user.tz != False:
                foto['timestamp'] = foto['timestamp'] - \
                                    datetime.datetime.utcoffset(datetime.datetime.now(pytz.timezone(self.env.user.tz)))
            self.env['fotocamera'].create(foto)
        collection.update_many({"id_edificio": self.id_edificio, "posizione": {'$exists': True},
                                "lettura": False}, {'$set': {"lettura": True}})
        return {
            'name': _('Immagini'),
            'domain': [('id_edificio', '=', self.id_edificio)],
            'view_type': 'form',
            'res_model': 'fotocamera',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def scritturaDB(self):
        view_id = self.env.ref('modulo_tirocinio.fotocamera_form_upload').id
        return {
            'name': 'Upload Immagini edificio',
            'view_type': 'form',
            'view_mode': 'form',
            'views': [(view_id, 'form')],
            'res_model': 'fotocamera',
            'view_id': view_id,
            'type': 'ir.actions.act_window',
            'target': 'new',
            'context': {'default_id_edificio': self.id_edificio}
        }