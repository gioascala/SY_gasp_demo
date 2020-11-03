from odoo import models, fields

class EdificioStorico(models.Model):
    _name = 'edificio.edificio'
    _description= 'Documenti della struttura'
    

    nome_edificio = fields.Char(string = 'Nome',required=True)
    indirizzo_edificio = fields.Char(string = 'Indirizzo',required=True)
    costruzione_edificio = fields.Char('Anno di costruzione') #serve per capire quando l'edificio è stato creato.
    località_edificio= fields.Char(string= 'Località', required=True)
    stile_edificio = fields.Char(string= 'Stile', required=True)
    altezza_edificio = fields.Integer('Altezza(m)')
    piani_edificio = fields.Integer('Piani')
    proprietario_edifico = fields.Char(string ='Proprietario',required=True)
    immagine_edificio = fields.Binary(string='Immagine',attachment=False)
    is_done = fields.Boolean(string= 'Done?', help='Quando la manutenzione è finita, Done deve essere spuntato')
    active = fields.Boolean(string = 'Active?', default=True, help='Quando Done viene spuntato, Active deve passare basso')

    name= fields.Char(string='ID_Edificio', required=True)
    
    notes= fields.Text(string='Sommario')
    fondazione_id = fields.Many2many('edificio.fondazioni',string='Tipo di fondazione')
    strutturaverticale_id= fields.Many2many('edificio.strutturaverticale', string = 'Tipo di strutturaV')
    strutturaorizzontale_id= fields.Many2many('edificio.strutturaorizzontale', string = 'Tipo di strutturaO')
    impiantiGas_id = fields.Many2many('edificio.impiantigas', string = 'Tipo di impianto gas')
    impiantisanitari_id = fields.Many2many('edificio.impiantidricisanitari',string='Tipo di impianto idrico sanitario')
    impiantielettrici_id = fields.Many2many('edificio.impiantielettrici', string='Tipo di impianto elettrico')
    impianticlim_id = fields.Many2many('edificio.impiantidiclimatizzazione',string= 'Tipo di impianto climatizzato')
    impiantisicurezza_id=fields.Many2many('edificio.impiantisicurezza',string='Tipo di impianto sicurezza')
    impiantisollevamento_id = fields.Many2many('edificio.impiantisollevamento',string='Tipo di impianto sollevamento')
    impiantitelecom_id = fields.Many2many('edificio.impiantitelecom',string='Tipo di impianto di telecomunicazione')
    sistemainterno_id = fields.Many2many('edificio.sistemainterno',string='Tipo di sistema interno')
    sistemaesterno_id = fields.Many2many('edificio.sistemaesterno',string='Tipo di sistema esterno')
    areaparcheggio_id = fields.Many2many('edificio.areaparcheggio',string= 'Tipo di area parcheggio')
    distribuzionenergiaelettrica_id = fields.Many2many('edificio.distribuzionenergiaelettrica',string ='Tipo di distribuzione')
    fornituraDistrAcqua_id = fields.Many2many('edificio.fornituradistracqua',string='Tipo di fornitura')
    guardiola_id = fields.Many2many('edificio.guardiola',string='Tipo di guardiola')
    segnaleticacartelliesterni_id = fields.Many2many('edificio.segnaleticacartelliesterni',string='Tipo di segnaletica')
    servizigenerali_id = fields.Many2many('edificio.servizigenerali',string='Tipo di servizio')
    valorizzazionearea_id = fields.Many2many('edificio.valorizzazionearea',string='Tipo di valorizzazione')
    verdesterno_id = fields.Many2many('edificio.verdesterno',string='Tipo di verde esterno')
    zonepedonaliesterne_id = fields.Many2many('edificio.zonepedonaliesterne',string='Tipo di zone pedonali')

    
    
    

