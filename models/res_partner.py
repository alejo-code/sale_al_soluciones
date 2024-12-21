# -*- coding: utf-8 -*-
# Copyright 2024 Alejandro Olano <Github@alejo-code>

from odoo import models, fields, api, SUPERUSER_ID, _


class ResPartner(models.Model):
    _inherit = "res.partner"

    vip = fields.Boolean(string="VIP", default=False)
    warn_vip = fields.Boolean(compute="_get_warn_vip", store=False)

    @api.model
    def _get_warn_vip(self):
        user = self.env["res.users"].search([("id", "=", self.env.user.id)])
        self.warn_vip = False

        if (
            user.has_group("sales_team.group_sale_manager")
            and self.env.user.id != SUPERUSER_ID
        ):
            self.warn_vip = True
