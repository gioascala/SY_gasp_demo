from odoo import models ,fields

class Zona_pedonali_esterne(models.Model):
    _name='zona_pedonali_esterne'

    unità_tecnologica = fields.Selection([("Pavimentazione bituminosa", "Pavimentazione bituminosa"), ("Pavimentazione cementizia gettata in opera o prefabbricata","Pavimentazione cementizia gettata in opera o prefabbricata"),("Pavimentazione in blocchi", "Pavimentazione in blocchi"), ("Pavimentazione in lastre di pietra","Pavimentazione in lastre di pietra"),("Pavimentazione in granito", "Pavimentazione in granito")])
    elemento_tecnico = fields.Text()