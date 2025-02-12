# Copyright 2020 Camptocamp
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Shopfloor - Batch Transfer Automatic Creation",
    "summary": "Create batch transfers for Cluster Picking",
    "version": "14.0.1.2.0",
    "development_status": "Alpha",
    "category": "Inventory",
    "website": "https://github.com/OCA/wms",
    "author": "Camptocamp, Odoo Community Association (OCA)",
    "maintainers": ["guewen"],
    "license": "AGPL-3",
    "application": False,
    "depends": [
        "shopfloor",
        "stock_packaging_calculator",  # OCA/stock-logistics-warehouse
        "product_packaging_dimension",  # OCA/product-attribute
        "product_total_weight_from_packaging",  # OCA/product-attribute
    ],
    "data": [
        "views/shopfloor_menu_views.xml",
    ],
    "installable": True,
}
