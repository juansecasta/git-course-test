# -*- coding: utf-8 -*-
{
    'name': "Gestion Taller",

    'summary': """
    Gestion vehiculos y Reparaciones 
""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Gestion Vehiculo',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
         'security/ir.model.access.csv',
        'data/data.xml',
        'views/vehiculo_view.xml',
        'views/order_reparacion_view.xml',
    ],

}
