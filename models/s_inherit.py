# -*- coding: utf-8 -*-

from odoo import api, fields, models



class evalsaleorder(models.Model):
    _inherit = 'sale.order'

    eval_newname = fields.Char('Customer Reference')
    eval_ref = fields.Char('Customer Reference')

