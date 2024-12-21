# -*- coding: utf-8 -*-
# Copyright 2024 Alejandro Olano <Github@alejo-code>

from odoo import models, fields, api
from datetime import datetime


class SaleOrderWizard(models.TransientModel):
    _name = "sale.order.wizard"
    _description = "Wizard para filtrar pedidos de ventas por vendedor y fecha"

    user_ids = fields.Many2many(
        comodel_name="res.users",
        string="Vendedores",
        help="Selecciona uno o más vendedores para filtrar los pedidos.",
    )
    date_from = fields.Date(string="Desde")
    date_to = fields.Date(string="Hasta")

    @api.model
    def _get_domain(self):
        """Genera el dominio dinámico basado en los criterios del wizard."""
        domain = []
        if self.user_ids:
            domain.append(("user_id", "in", self.user_ids.ids))
        if self.date_from:
            domain.append(("date_order", ">=", self.date_from))
        if self.date_to:
            domain.append(("date_order", "<=", self.date_to))
        return domain

    def action_filter_sales(self):
        """Filtra los pedidos de ventas y los imprime en la consola."""
        domain = self._get_domain()
        sales_orders = self.env["sale.order"].search(domain)
        for order in sales_orders:
            print(
                f"Pedido: {order.name}, Vendedor: {order.user_id.name}, Fecha: {order.date_order}"
            )
        return {"type": "ir.actions.act_window_close"}
