# -*- coding: utf-8 -*-
# from odoo import http


# class Edificio(http.Controller):
#     @http.route('/edificio/edificio/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/edificio/edificio/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('edificio.listing', {
#             'root': '/edificio/edificio',
#             'objects': http.request.env['edificio.edificio'].search([]),
#         })

#     @http.route('/edificio/edificio/objects/<model("edificio.edificio"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('edificio.object', {
#             'object': obj
#         })
