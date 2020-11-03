from odoo import models ,fields

class Aree_di_parcheggio(models.Model):
    _name='aree_di_parcheggio'

    unità_tecnologica= fields.Selection([("Pavimentazione bituminosa", "Pavimentazione bituminosa"), ("Pavimentazione in calcestruzzo bituminoso", "Pavimentazione in calcestruzzo bituminoso"),("Pavimentazione in calcestruzzo", "Pavimentazione in calcestruzzo")])
    elemento_tecnico = fields.Text()