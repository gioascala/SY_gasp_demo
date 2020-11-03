# -*- coding: utf-8 -*-
# from odoo import http


# class ModExt(http.Controller):
#     @http.route('/mod_ext/mod_ext/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mod_ext/mod_ext/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mod_ext.listing', {
#             'root': '/mod_ext/mod_ext',
#             'objects': http.request.env['mod_ext.mod_ext'].search([]),
#         })

#     @http.route('/mod_ext/mod_ext/objects/<model("mod_ext.mod_ext"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mod_ext.object', {
#             'object': obj
#         })
