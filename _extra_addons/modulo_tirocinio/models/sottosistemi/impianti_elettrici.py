from odoo import models, fields, api, _

class Impianti_elettrici(models.Model):
    _name = 'impianti_elettrici'

    unità_tecnologica=fields.Selection([("Utilizzatori Elettrici","Utilizzatori Elettrici"),("Rete Distribuzione","Rete Distribuzione"),("Impianto protezione scariche atmosferiche","Impianto protezione scariche atmosferiche"),("Impianto Rifasamento","Impianto Rifasamento"),("Impianto terra","Impianto terra"),("Quadro Zona","Quadro Zona"),("Quadro Generale","Quadro Generale"),("Centrale energia di emergenza","Centrale energia di emergenza"),("Cabina trasformazione","Cabina trasformazione"),("Gruppo continuità","Gruppo continuità")])
    elemento_tecnico = fields.Text()