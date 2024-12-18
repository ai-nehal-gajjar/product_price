# -*- coding: utf-8 -*-

{
    # App information
    'name': 'Product Price',
    'category': 'Sales',
    'summary': 'Product Price',
    'version': '17.0.1.0.0',
    'depends': [
        'sale_management',
        'stock',
    ],

    'data': [
        'security/product_price_security.xml',
        'views/sale_order_views.xml',
        'views/product_template_views.xml',
    ],

    # Author
    'author': 'Aktiv Software Pvt. Ltd.',
    'website': 'https://www.aktivsoftware.com/',
    'maintainer': 'Aktiv Software Pvt. Ltd.',

    # Technical
    'installable': True,
    'auto_install': False,
    'application': True,

}
