from odoo import models,fields

class DocumentiPDF(models.Model):
    _name= 'modulo_pdf.docupdf'
    _description='Documenti PDF'

    documento_pdf = fields.Binary(string='Documento')

class DocumentoUserInherit(models.Model):
    _inherit = "hr.employee"
    documento_nome = fields.Many2many("hr.employee",string='Documento')
