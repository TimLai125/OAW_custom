# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limted T/A OSCG
# Copyright 2017 eHanse
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Partner Stock Offer',
    'version': '8.0.0.9.0',
    'author': 'eHanse,oa-trade,Quartile Limited,',
    'website': 'https://www.odoo-asia.com',
    'category': 'Product',
    'depends': [
        'product',
        'product_offer',
        'model_security_adjust_oaw',
        'supplier_stock'

    ],
    'description': """
        Creates a kanban view next to product_offer views based on supplier_stock model 'supplier_stock.py'
    """,
    'data': [
        'views/partner_stock_template_views.xml',
    ],
    'post_init_hook': '_update_partner_offer_fields',
    'installable': True,
}
