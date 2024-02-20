from odoo import models, fields, api,_
from datetime import datetime, timedelta

class cash(models.Model):
    _name = 'cash.flow'
    name = fields.Char(String="Name")
    fecha_i = fields.Date(String="Fecha Inicial")
    fecha_f = fields.Date(String="Fecha Final")
    sale = fields.Monetary(string='Acumulado de Ventas', currency_field='currency_id', compute='_onchange_ventas')
    currency_id = fields.Many2one('res.currency', string='Moneda', default=lambda self: self.env.company.currency_id)

    @api.onchange('currency_id')
    def _onchange_currency_id(self):
        if self.currency_id:
            self.sale.currency_id = self.currency_id.id

    def _onchange_ventas(self):
        for record in self:
            if record.x_name:  
                nuevo = self.env['sale.order'].search([('date_order', '>=', record.fecha_i),('date_order', '<=', record.fecha_f)])
                total = sum(nuevo.mapped('amount_total'))
                record.sale = total
            else:
                record.sale = 0
