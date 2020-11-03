# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloPdf(http.Controller):
#     @http.route('/modulo_pdf/modulo_pdf/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_pdf/modulo_pdf/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_pdf.listing', {
#             'root': '/modulo_pdf/modulo_pdf',
#             'objects': http.request.env['modulo_pdf.modulo_pdf'].search([]),
#         })

#     @http.route('/modulo_pdf/modulo_pdf/objects/<model("modulo_pdf.modulo_pdf"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_pdf.object', {
#             'object': obj
#         })
