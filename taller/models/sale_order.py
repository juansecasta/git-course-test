from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def default_get(self, fields_list):
        res=super(SaleOrder, self).default_get(fields_list)
        res.update({'validity_date': fields.Date.today()})


        # products_search = self.env["product.product"].search([])
        # products_browse = self.env["product.product"].browse(
        #     products_search.ids
        # )
        # products_sr = self.env["product.product"].search_read(
        #     [], # domain[()]
        #     ['id', 'name',
        #      'lst_price'], order='id,name')

        return res

    @api.model
    def create(self, values):





        record = super(SaleOrder, self).create(values)
        # Preparamos la logica que quieras
        # Si el cliente tiene correo
        if record.partner_id.email:
            #suscribimos al cliente
            record.message_subscribe([record.partner_id.id])
            message = "Nuevo Presupuesto creado"
            record.message_post(body=message)
        return record






