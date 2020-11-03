from odoo import models , fields,api


class Prodotti(models.Model):
    _inherit='product.product'

    test= fields.Char(default="Non verificato",readonly=True)

    def check_qualità(self):
            view_id = self.env.ref('controllo_qualità.produzione_form_poupup').id
            context = self._context.copy()
            return {
                'name': 'Controllo Qualità',
                'view_type': 'form',
                'view_mode': 'tree',
                'views': [(view_id, 'form')],
                'res_model': 'product.product',
                'view_id': view_id,
                'type': 'ir.actions.act_window',
                'res_id': self.id,
                'target': 'new',
                'context': context,
            }

    def superato(self):
        self.write({'test':'Superato'})

    def fallito(self):
        self.write({'test':'Fallito'})



