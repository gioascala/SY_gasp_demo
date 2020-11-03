from odoo import models , fields

class Guasti(models.Model):
    _name='guasti'

    coperture=fields.Many2many('g_coperture')
    finiture_interne=fields.Many2many('g_finiture_interne_murarie')
    fondazioni=fields.Many2many('g_fondazioni')
    infissi_esterni=fields.Many2many('g_infissi_esterni')
    muri_esterni=fields.Many2many('g_muri_esterni')
    partizioni_fisse=fields.Many2many('g_partizioni_fisse')
    pavimentazioni=fields.Many2many('g_pavimentazioni')
    strutture_orizzontali=fields.Many2many('g_strutture_orizzontali')
    strutture_verticali=fields.Many2many('g_strutture_verticali')