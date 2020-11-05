# -*- coding: utf-8 -*-

from odoo import models, fields

class NewModule(models.Model):
    _inherit = 'product.template'

    price_2 = fields.Monetary(string="Precio 2")


