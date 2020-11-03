from odoo import models,fields,api, _
from . import connettore
import base64
import datetime
from PIL import Image,ExifTags
from io import BytesIO

class Fotocamera(models.Model):
    _name='fotocamera'

    posizione=fields.Selection([('Superficie esterna','Superficie esterna'),('Superficie interna','Superficie interna'),('Tetto','Tetto')])
    id_edificio=fields.Text()
    timestamp=fields.Datetime()
    image=fields.Binary()
    image_upload=fields.Many2many('ir.attachment',delete="oncascade")

    def carica(self):
        collection=connettore.connessione()
        for image in self.image_upload:
            if(Image.open(BytesIO(base64.b64decode(image.datas)))._getexif() == None):
                data=None
            else:
                data = datetime.datetime.strptime(Image.open(BytesIO(base64.b64decode(image.datas))).getexif()[36867],'%Y:%m:%d %H:%M:%S')
            dict = {'posizione': self.posizione, 'id_edificio': self.id_edificio, 'timestamp': data,'image': base64.b64decode(image.datas), 'lettura': False}
            collection.insert(dict)
        self.env['fotocamera'].search([('id', '=', self.id)]).unlink()

