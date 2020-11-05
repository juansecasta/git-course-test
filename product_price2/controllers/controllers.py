# -*- coding: utf-8 -*-
# from odoo import http


# class ProductPrice2(http.Controller):
#     @http.route('/product_price2/product_price2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_price2/product_price2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_price2.listing', {
#             'root': '/product_price2/product_price2',
#             'objects': http.request.env['product_price2.product_price2'].search([]),
#         })

#     @http.route('/product_price2/product_price2/objects/<model("product_price2.product_price2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_price2.object', {
#             'object': obj
#         })
