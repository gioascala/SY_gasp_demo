from odoo import models, fields

class Guardiola(models.Model):
    _name = 'edificio.guardiola'
    _description ='Sistema delle pertinenze'

    unità_tecnologica = fields.Char(String='Unità tecnologica', required=True)
    elemento_tecnico = fields.Char(String='Elemento tecnico')

    name= fields.Char(string='Guardiola ID', required=True)

    edificio_id = fields.Many2many('edificio.edificio',string='Edificio',required=True)
    notes= fields.Text(string='Note di servizio')
    tipo_guasto = fields.Char(string = 'Tipo di guasto')
    causa_guasto = fields.Text(string = 'Causa del guasto')
    segnali_deter = fields.Text(string =  'Segnali di deterioramento')
    
