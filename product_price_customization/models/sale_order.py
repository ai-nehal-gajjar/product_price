# -*- coding: utf-8 -*-

from odoo import fields, models, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    price_base_on = fields.Selection([
        ('once', 'Once'),
        ('monthly', 'Monthly'),],
        string="Price Base On"
    )

    @api.onchange('price_base_on')
    def _onchange_so_price_base_on(self):
        if self.order_line:
            for order_line in self.order_line:
                if order_line:
                    if self.price_base_on == 'once':
                        order_line.product_template_id.price_base_on = 'once'
                    if self.price_base_on == 'monthly':
                        order_line.product_template_id.price_base_on = 'monthly'
