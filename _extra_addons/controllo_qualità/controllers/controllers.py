# -*- coding: utf-8 -*-
# from odoo import http


# class ControlloQualità(http.Controller):
#     @http.route('/controllo_qualità/controllo_qualità/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/controllo_qualità/controllo_qualità/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('controllo_qualità.listing', {
#             'root': '/controllo_qualità/controllo_qualità',
#             'objects': http.request.env['controllo_qualità.controllo_qualità'].search([]),
#         })

#     @http.route('/controllo_qualità/controllo_qualità/objects/<model("controllo_qualità.controllo_qualità"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('controllo_qualità.object', {
#             'object': obj
#         })
