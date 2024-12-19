# -*- coding: utf-8 -*-

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    price_base_on = fields.Selection([
        ('once', 'Once'),
        ('monthly', 'Monthly')],
        string="Price Base On",
        required=True,
        default='monthly'
    )

    def update_product_price_base_on(self):
        """Update the price base on"""
        for order_line in self.order_line:
            order_line.product_template_id.price_base_on = self.price_base_on

    def write(self, values):
        """For update the product template price base on the order.

        :param values:
        :return:
        """
        result = super(SaleOrder, self).write(values)
        if values.get('price_base_on'):
            self.update_product_price_base_on()
        return result
