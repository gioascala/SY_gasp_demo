from odoo import models,fields,api

class EdificioTask(models.Model):
    _inherit = 'edificio.edificio'
   
    
class CronologiaTask(models.Model):
    _inherit = 'edificio.cronologia'
class OperatoriTask(models.Model):
    _inherit ='edificio.operatori'
    operatore1_id = fields.Many2one(help='Figura principale di un processo manutentivo strutturato e primo attore coinvolto nelle scelte dirette')
    operatore2_id = fields.Many2one(help='Si dota degli strumenti di gestione rivolti a comprendere il corretto svolgimento delle azioni manutentive, oltre la corretta lettura dei segnali sintomo di un cattivo sviluppo delle procedure impostate')
    operatore3_id = fields.Many2one(help='che può trovare le indicazioni oggettive per processi manutentivi a carico di un insieme di elementi tecnici o di una molteplicità di sistemi.')
    operatore4_id = fields.Many2one(help='al quale possono essere fornite le indicazioni per comprendere l’esatto rendimento – non solo economico – e lo stato di conservazione del proprio patrimonio.')
    
