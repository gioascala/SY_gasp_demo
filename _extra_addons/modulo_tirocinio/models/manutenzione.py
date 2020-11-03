from odoo import models,fields,api,_
import datetime
import logging

_logger = logging.getLogger(__name__)

class Manutenzione(models.Model):
    _name="manutenzione"

    id_edificio=fields.Many2one('edificio',string="Edificio",required=True)
    data_manutenzione=fields.Datetime(required=True)
    # syl4_data_creazione_manutenzione=fields.Date(string='Data Creazione manutenzione',default='New')
    persone=fields.One2many('addetto_custom','syl4_manutenzione','Addetti', copy=True)
    tipo=fields.Selection([('Correttiva', 'Correttiva'), ('Periodica', 'Periodica')],required=True)
    descrizione_intervento=fields.Text(required=True)

    def mail(self):
        _logger.info('INVIO EMAIL....')
        for persona in self.persone:
            body=f"Salve {persona.name} ,<br/>Bisogna effettuare la manutenzione {self.tipo.lower()} all'edificio {self.id_edificio.id_edificio} il giorno {self.data_manutenzione}." \
                 f"<br/>Descrizione della manutenzione:<br/>{self.descrizione_intervento}<br/>Buona giornata."
            _logger.info(f'body: \n {body}')
            mail_template=self.env['mail.template'].browse(self.env.ref('modulo_tirocinio.email_di_avviso').id)
            mail_template.write({'email_to':persona.login,'body_html':body })
            mail_template.send_mail(self.id,force_send=True)

    def invio_mail(self):
        for manutenzione in self.env['manutenzione'].search(
                [('data_manutenzione', '=', datetime.date.today() + datetime.timedelta(days=4))]):
            manutenzione.mail()

    # @api.model
    # def create(self, vals):
    #     # definisco il codice
    #     if vals.get('syl4_data_creazione_manutenzione', 'New') == 'New':
    #         vals['syl4_data_creazione_manutenzione'] = datetime.date.today()
    #         _logger.info('CREATE - EMAIL....')
    #     result = super(Manutenzione, self).create(vals)
    #     return result