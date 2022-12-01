# Copyright 2022 Brian McMaster <brian@mcmpest.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
from odoo import fields, models


class ShopfloorAppUserProfile(models.Model):
    _name = "shopfloor.app.user.profile"

    user_id = fields.Many2one("res.users", string="User")
    shopfloor_app_id = fields.Many2one("shopfloor.app", string="Shopfloor App")
    profile_id = fields.Many2one("shopfloor.profile", string="Shopfloor Default Profile")
