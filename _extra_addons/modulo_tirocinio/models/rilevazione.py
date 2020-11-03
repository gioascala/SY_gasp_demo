from odoo import models,fields,api, _

class Rilevazione(models.Model):
    _name='rilevazione'

    timestamp=fields.Datetime()
    id_edificio = fields.Char('Edificio')
    id_rilevazione=fields.Char(string="Id Rilevazione", readonly=True , default=lambda self: _('New') )

    @api.model
    def create(self, vals):
        if vals.get('id_rilevazione', _('New')) == _('New'):
            vals['id_rilevazione']= self.env['ir.sequence'].next_by_code('rilevazioni.sequenza') or _('New')
        result= super(Rilevazione, self).create(vals)
        return result

