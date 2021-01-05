# -*- coding: utf-8 -*-

from odoo import models, fields

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    vendor_type = fields.Selection(
        string="vendor_type",
        selection=[
        ('type1','type1'),
        ('type2', 'type2'),
    ]
    )

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    origin = fields.Char(string='Origin')

