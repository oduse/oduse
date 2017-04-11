# -*- coding: utf-8 -*-

from odoo import api, models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    plat_code = fields.Char(string=u'交易平台编码', help=u'该药品在药品交易平台的编码。')
    model = fields.Char(u'药品规格', help=u'药品的规格。')
    is_puyao = fields.Selection([('P', "普药"),('N', "新药"),], default='P')
    buyer = fields.Many2one('res.users', ondelete='set null', string=u'采购员', required=True)

    manufacturing_enterprise = fields.Char(u'生产企业', help=u'药品生产企业。')
    bid_enterprise = fields.Char(u'投标企业', help=u'药品投标企业。')
    the_form_of_a_drag = fields.Char(string=u'剂型')
    lis_number = fields.Char(u'批准文号', help=u'药品的批准文号。')
    zstype = fields.Char(u'药品分类', help=u'针对每个公司对药品的分类信息。')
    product_class = fields.Char(u'目录属性', help=u'药品的目录属性。')

    packing = fields.Integer(u'装箱量', help=u'药品的装箱量。如一箱多少盒。')
    package_count = fields.Integer(u'包装数', help=u'包装数量，一般只件装里面的下一节单位数量。比如一件20盒。')
    dk_price = fields.Float(string=u'打款价', digits=(18, 4), default=0)
    floor_price = fields.Float(string=u'底价', digits=(18, 4), default=0)
    cesd = fields.Float(string=u'差额税点', digits=(18, 4), default=0)
    txsj = fields.Float(string=u'提现税金', digits=(18, 4), default=0)
    fkamount = fields.Float(digits=(18, 4), string=u'返款额', default=0)
    fk_cycle = fields.Float(string=u'返款周期', digits=(18, 0), default=0)
    fkfangshi = fields.Selection([('1', "现款"),('2', "实销月结"),('3', "送二结一"),('4', "账期"),], default='1')
    xsht = fields.Char(string=u'销售合同号')
