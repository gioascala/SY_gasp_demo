from odoo import models , fields,api


class Prodotti_in_ingresso(models.Model):
    _name='prodotti_in_ingresso'

    prodotto= fields.Many2one("product.template", required=True,ondelete='cascade')
    fornitore= fields.Many2one("res.partner", required=True,ondelete='cascade')
    peso=fields.Text(redonly=True,compute="get_peso")
    volume= fields.Text(redonly=True, compute="get_volume")

    @api.depends('prodotto')
    def get_peso(self):
        for rec in self:
            rec.peso= rec.prodotto.weight

    @api.depends('prodotto')
    def get_volume(self):
        for rec in self:
            rec.volume = rec.prodotto.volume
