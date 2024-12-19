# -*- coding: utf-8 -*-

from odoo import fields, models, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    price_base_on = fields.Selection([
        ('once', 'Once'),
        ('monthly', 'Monthly')],
        string='Price Base On',
    )

    @api.model_create_multi
    def create(self, vals_list):
        """For adding price base on order price base on.

        :param vals_list:
        :return:
        """
        for vals in vals_list:
            sale_order_id = self.order_id.browse(vals.get('order_id', False))
            if sale_order_id:
                vals['price_base_on'] = sale_order_id.price_base_on
        result = super(SaleOrderLine, self).create(vals_list)
        self.update_price_subtotal()
        return result

    @api.onchange('price_base_on')
    def _onchange_sol_price_base_on(self):
        """Update price unit base on the price base on."""
        if self.price_base_on:
            self.update_price_subtotal()

    def update_price_subtotal(self):
        """For Update price unit base on security group."""
        total_prod_price = 0.0
        if self.user_has_groups(' \
                product_price_customization.group_update_base_on_so_line'):
            if self.price_base_on == 'once':
                total_prod_price = self.product_template_id.list_price
            elif self.price_base_on == 'monthly':
                total_prod_price = self.product_template_id.list_price * 12
            self.price_unit = total_prod_price
