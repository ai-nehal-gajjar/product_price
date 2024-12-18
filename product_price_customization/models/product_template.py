# -*- coding: utf-8 -*-

from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    price_base_on = fields.Selection([
        ('once', 'Once'),
        ('monthly', 'Monthly'),],
        string="Price Base On"
    )
