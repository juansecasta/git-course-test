# -*- coding: utf-8 -*-

from odoo import api, models, fields, exceptions


class OrderReparacion(models.Model):
    _name = 'taller.orden.reparacion'
    _description = 'Gestion ordenes reparación'

    state = fields.Selection([
        ('nuevo', 'Nuevo'),
        ('confirmado', 'confirmado'),
        ('realizado', 'Realizado'),
        ('cancelado', 'Cancelado')
    ], string='Estado', readonly=True, index=True, copy=False, default='draft',
        tracking=True)
    # trackin va haciendo regitro de la modificaciones que voy haciendo

    active = fields.Boolean(string='Active', default=True)
    name = fields.Char(string='Name',
                       help='Introduce el nombre',
                       default='Nueva Orden Reparacion')

    partner_id = fields.Many2one('res.partner', string="Cliente")
    reparacion_line_ids = fields.One2many(
        comodel_name='taller.orden.reparacion.line',
        inverse_name='reparacion_id',
        string='Lineas Reparacion'
    )

    notas = fields.Html(string="Notas")

    READONLY_STATES = {
        'nuevo': [('readonly', False)],
        'confirmado': [('readonly', True)],
        'cancelado': [('readonly', False)],
    }

    company_id = fields.Many2one('res.company', 'Company', requiered=True,
                                 index=True, states=READONLY_STATES,
                                 default=lambda self: self.env.company.id)

    @api.model
    def create(self, vals):
        new_seq_name = self.env['ir.sequence'].next_by_code(
            'orden.reparacion') or 'New'
        vals.update(name=new_seq_name)
        res = super(OrderReparacion, self).create(vals)
        return res

    def confirm(self):
        self.write({'state': "confirmado"})


class OrderReparacionLine(models.Model):
    _name = 'taller.orden.reparacion.line'

    active = fields.Boolean(string='Active', default=True)
    name = fields.Char(string='Nombre',
                       help='Introduce el nombre',
                       default='Nueva Linea Reparacion')
    reparacion_id = fields.Many2one(comodel_name='taller.orden.reparacion')
    vehiculo_id = fields.Many2one('taller.vehiculo', string="Vehiculo")





class VehicleInherit(models.Model):
    # si se agrega _name, creara una nueva tabla en postgreSQL
    _inherit = 'taller.vehiculo'

    #marca = fields.char('Marca')

