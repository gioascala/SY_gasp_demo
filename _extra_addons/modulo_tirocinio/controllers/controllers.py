# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloTirocinio(http.Controller):
#     @http.route('/modulo_tirocinio/modulo_tirocinio/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_tirocinio/modulo_tirocinio/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_tirocinio.listing', {
#             'root': '/modulo_tirocinio/modulo_tirocinio',
#             'objects': http.request.env['modulo_tirocinio.modulo_tirocinio'].search([]),
#         })

#     @http.route('/modulo_tirocinio/modulo_tirocinio/objects/<model("modulo_tirocinio.modulo_tirocinio"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_tirocinio.object', {
#             'object': obj
#         })
