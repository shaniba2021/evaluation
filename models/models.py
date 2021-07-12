# -*- coding: utf-8 -*-

from odoo import fields, models, api


class evaluationcustomer(models.Model):
     _name = 'evaluation.customer'
     _description = 'evaluation.customer'



     name = fields.Char('Customer')
     ch_number = fields.Integer('Check Number')
     amount = fields.Integer('Amount')
     phone = fields.Integer('mobile No')
     state = fields.Selection([('draft','Draft'),('confirm','Confirmed'),('cancel','Cancelled')],
                              string='States', default='draft')

     def btn_confirm(self):
           print("......................................................................................")
           self.state = 'confirm'

     def btn_cancel(self):
           print("......................................................................................")
           self.state = 'cancel'

     def btn_reset(self):
         print("......................................................................................")
         self.state = 'draft'

class newcustomer(models.Model):
     _name = 'new.customer'
     _description = 'new.customer'

     @api.onchange("cust_name")
     def onchange_cust_name(self):
          phone = self.cust_name.phone
          self.nphone = phone



     name = fields.Char('customer')
     nphone = fields.Integer('Mobile No')
     cust_name = fields.Many2one('evaluation.customer','customer name')

     #def btn_confirm(self):
         # phone = self.nphone


