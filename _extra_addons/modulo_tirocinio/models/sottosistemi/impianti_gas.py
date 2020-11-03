from odoo import models , fields , api , _

class Impianti_gas(models.Model):
    _name='impianti_gas'

    unità_tecnologica=fields.Selection([("Tubazioni","Tubazioni"),("Tubo flessibile","Tubo flessibile"),("Dispositivi di evacuazione dei prodotti della combustione","Dispositivi di evacuazione dei prodotti della combustione"),("Apparecchi Utilizzatori","Apparecchi Utilizzatori"),("Rubinetto per Gas","Rubinetto per Gas"),("Serbatoi di stoccaggio","Serbatoi di stoccaggio")])
    elemento_tecnico = fields.Text()