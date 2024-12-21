# -*- coding: utf-8 -*-
# Copyright 2024 Alejandro Olano <Github@alejo-code>

{
    "name": "Sales Extension - VIP",
    "version": "14.0.0.1",
    "category": "Sales",
    "author": "Tu nombre o tu empresa",
    "depends": ["sale", "sales_team"],
    "data": [
        "data/product_pricelist_data.xml",
        "views/res_partner_view.xml",
        "views/sale_order_view.xml",
        "wizard/sale_order_wizard_view.xml",
    ],
    "installable": True,
    "application": False,
}
