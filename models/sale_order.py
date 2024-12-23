# -*- coding: utf-8 -*-
# Copyright 2024 Alejandro Olano <Github@alejo-code>


from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    vip = fields.Boolean(string="VIP", related="partner_id.vip", store=True)

    @api.onchange("partner_id")
    def _onchange_partner_id(self):
        if self.partner_id.vip:
            tarifa_vip = self.env.ref(
                "sale_al_soluciones.vip_discount", raise_if_not_found=False
            )
            if tarifa_vip:
                self.partner_id.write({"property_product_pricelist": tarifa_vip.id})
