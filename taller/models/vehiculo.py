# -*- coding: utf-8 -*-

from odoo import api, models, fields, exceptions


class Vehicle(models.Model):
    _name = 'taller.vehiculo'
    _description = 'Gestion Vehiculos Odoo'
    name = fields.Char(string='Name', help='Introduce el nombre', size=20,
                       default='Nuevo')
    active = fields.Boolean(string='Active', default=True)
    matricula = fields.Char('Placa')

    # validacion unico por sql_constraint
    _sql_constraints = [
        ('vehiculo_name_uniq',
         'unique (name)',
         'El nombre debe ser unico!')
    ]

    tag_ids = fields.Many2many(comodel_name='vehiculo.tag')

    # validación por api constraint
    @api.constrains('matricula')
    def _check_matricula(self):
        # Comprobamos si es unica
        domain = [('matricula', '=', self.matricula),
                  ('id', '!=', self.id)]
        vehiculos = self.search(domain)

        if vehiculos:
            raise exceptions.ValidationError('Matricula duplicada')


class VehiculoTag(models.Model):
    _name = 'vehiculo.tag'

    name = fields.Char(string="Name")