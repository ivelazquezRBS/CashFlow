# -*- coding: utf-8 -*-
# from odoo import http


# class HerenciaMrp(http.Controller):
#     @http.route('/herencia_mrp/herencia_mrp', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/herencia_mrp/herencia_mrp/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('herencia_mrp.listing', {
#             'root': '/herencia_mrp/herencia_mrp',
#             'objects': http.request.env['herencia_mrp.herencia_mrp'].search([]),
#         })

#     @http.route('/herencia_mrp/herencia_mrp/objects/<model("herencia_mrp.herencia_mrp"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('herencia_mrp.object', {
#             'object': obj
#         })
