# Copyright 2019 Camptocamp (https://www.camptocamp.com)
{
    "name": "Stock Dynamic Routing",
    "summary": "Dynamic routing of stock moves",
    "author": "Camptocamp, BCIM, Odoo Community Association (OCA)",
    "maintainers": ["jbaudoux"],
    "website": "https://github.com/OCA/wms",
    "category": "Warehouse Management",
    "version": "14.0.1.1.1",
    "license": "AGPL-3",
    "depends": ["stock", "stock_helper"],
    "demo": [
        "demo/stock_location_demo.xml",
        "demo/stock_picking_type_demo.xml",
        "demo/stock_routing_demo.xml",
    ],
    "data": ["views/stock_routing_views.xml", "security/ir.model.access.csv"],
    "installable": True,
    "development_status": "Beta",
}
