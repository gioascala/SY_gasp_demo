from odoo import models,fields

class CronologiaLavori(models.Model):
    _name = 'edificio.cronologia'
    _description = 'Cronologia della manutenzione'

    name = fields.Integer(string = 'Codice',required=True)
    edificio_id = fields.Many2one('edificio.edificio',string='Edificio',required=True)
    data_fine = fields.Many2one('calendar.event',string='Data di inizio manutenzione',required= True)
    data_fine2 = fields.Many2one('calendar.event',string='Data di fine manutenzione',required= True)
    stop_iniz = fields.Date(string = 'Data di inizio pausa')
    stop_fin = fields.Date(string = 'Data di fine pausa')
    pausa_text = fields.Text(string='Motivazione della pausa')
    
    
