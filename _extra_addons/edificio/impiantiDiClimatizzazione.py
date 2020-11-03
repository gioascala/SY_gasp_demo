from odoo import models, fields

class ImpiantiClim(models.Model):
    _name = 'edificio.impiantidiclimatizzazione'
    _description ='Sistema tecnologico'

    unità_tecnologica = fields.Char(String='Unità tecnologica', required=True)
    elemento_tecnico = fields.Char(String='Elemento tecnico', required=True)

    name= fields.Char(string='ImpiantiClim ID', required=True)

    edificio_id = fields.Many2many('edificio.edificio',string='Edificio',required=True)
    notes= fields.Text(string='Note di servizio')
    tipo_guasto = fields.Char(string = 'Tipo di guasto')
    causa_guasto = fields.Text(string = 'Causa del guasto')
    segnali_deter = fields.Text(string =  'Segnali di deterioramento')
    
     
        
        
