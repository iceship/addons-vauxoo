#!/usr/bin/python
# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#    Copyright (C) OpenERP Venezuela (<http://openerp.com.ve>).
#    All Rights Reserved
###############Credits######################################################
#    Coded by: Vauxoo C.A.           
#    Planified by: Nhomar Hernandez
#    Audited by: Vauxoo C.A.
#############################################################################
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
################################################################################

import time
from osv import fields, osv
import decimal_precision as dp
from tools.translate import _
import netsvc

class wh_iva_doc(osv.osv):
    _inherit = 'account.wh.iva'

    
    def check_state_draft(self, cr, uid, ids, context=None):
        '''
        Check invoice state to not move in state 
        '''
        iva_brw = self.browse(cr,uid,ids,context=context)[0]
        line_obj = self.pool.get('account.wh.iva.line')
        
        for i in self.browse(cr,uid,ids,context=context)[0].wh_lines:
            if i.invoice_id.state in ['draft','cancel']:
                return False

        return True
    
    def check_state_cancel(self, cr, uid, ids, context=None):
        '''
        Check invoice state to not move in state
        '''
        iva_brw = self.browse(cr,uid,ids,context=context)[0]
        
        for i in self.browse(cr,uid,ids,context=context)[0].wh_lines:
            if i.invoice_id.state == 'cancel':
                return False

        return True
    
wh_iva_doc()