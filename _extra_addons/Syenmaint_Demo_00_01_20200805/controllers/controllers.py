# -*- coding: utf-8 -*-
from odoo import http

class Syenmaint(http.Controller):
    @http.route('/syenmaint/syenmaint/', auth='public')
    def index(self, **kw):
     return "Hello, world"

    @http.route('/syenmaint/syenmaint/objects/', auth='public')
    def list(self, **kw):
     return http.request.render('syenmaint.listing', {
         'root': '/syenmaint/syenmaint',
         'objects': http.request.env['syenmaint.syenmaint'].search([]),
     })

    @http.route('/syenmaint/syenmaint/objects/<model("syenmaint.syenmaint"):obj>/', auth='public')
    def object(self, obj, **kw):
     return http.request.render('syenmaint.object', {
         'object': obj
     })