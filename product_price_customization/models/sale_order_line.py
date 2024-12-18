# -*- coding: utf-8 -*-

from odoo import fields, models, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    price_base_on = fields.Selection([
        ('once', 'Once'),
        ('monthly', 'Monthly'),],
        string='Price Base On',
        compute='_compute_price_base_on',
        store=True
    )

    @api.onchange('price_base_on')
    def _onchange_sol_price_base_on(self):
        if self.user_has_groups(' \
                product_price_customization.group_update_base_on_so_line'):
            self.update_price_subtotal()

    @api.depends('product_template_id.price_base_on')
    def _compute_price_base_on(self):
        self.price_base_on = ''
        for record in self:
            if self.product_template_id:
                for product_template_id in self.product_template_id:
                    if product_template_id.price_base_on == 'once':
                        record.price_base_on = 'once'

                    if product_template_id.price_base_on == 'monthly':
                        record.price_base_on = 'monthly'
                    if self.user_has_groups(' \
                            product_price_customization.group_update_base_on_so_line'):
                        self.update_price_subtotal()

    def update_price_subtotal(self):
        total_prod_price = 0.0
        for price_base in self:
            if price_base.price_base_on == 'once':
                total_prod_price = price_base.price_unit \
                                   * price_base.product_uom_qty
                price_base.price_subtotal = total_prod_price
            if price_base.price_base_on == 'monthly':
                total_prod_price = price_base.price_unit \
                                   * price_base.product_uom_qty \
                                   * 12
                price_base.price_subtotal = total_prod_price
