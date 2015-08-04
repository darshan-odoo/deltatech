# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2015 Deltatech All Rights Reserved
#                    Dorin Hongu <dhongu(@)gmail(.)com       
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api, _
import openerp.addons.decimal_precision as dp
from openerp.exceptions import   Warning, RedirectWarning

"""
class stock_warehouse(models.Model):
    _inherit = "stock.warehouse"
    
    user_id = fields.Many2one('res.users', string='Manager') 

 
class stock_location(models.Model):
    _inherit = "stock.location"
    
    user_id = fields.Many2one('res.users', string='Manager') 
"""
 
class stock_picking(models.Model):
    _inherit = "stock.picking"



    
    @api.multi
    def check_authorization_transfer(self):
        group_ext_id = 'deltatech_rec_access.group_stock_no_transfer' 
        res =  self.env['res.users'].has_group(group_ext_id)
        if res:
            raise Warning(_('You can not have authorization transfer.'))
        return True
 
    @api.cr_uid_ids_context
    def do_enter_transfer_details(self, cr, uid, picking, context=None):
        self.check_authorization_transfer(cr, uid, picking, context)
        return super(stock_picking, self).do_enter_transfer_details( cr, uid, picking, context )
 
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: