from odoo import models, fields,api,_

class Rilevazione_Sensore(models.Model):
    _name='rilevazione_sensore'

    id_sensore=fields.Char()
    valore=fields.Float()
    tipo_sensore=fields.Text('Tipo di sensore')
    id_rilevazione=fields.Many2one('rilevazione',string='Id Rilevazione',ondelete='cascade')

