# -*- coding: utf-8 -*-
# Copyright 2024 Alejandro Olano <Github@alejo-code>

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    vip = fields.Boolean(
        string="VIP", default=False, groups="sales_team.group_sale_manager"
    )
