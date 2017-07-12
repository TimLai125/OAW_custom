# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limted T/A OSCG
# Copyright 2017 eHanse
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Product Offer Filter',
    'version': '8.0.1.2.1',
    'author': 'Rooms For (Hong Kong) Limited T/A OSCG, eHanse',
    'website': 'https://www.odoo-asia.com',
    'category': 'Product',
    'depends': [
        'product',
        'sale_stock',
        'sale_line_quant_extended',
        'supplier_stock',
    ],
    'description': """
    """,
    'data': [
        'views/product_offer_filter.xml',
    ],
    'installable': True,
}