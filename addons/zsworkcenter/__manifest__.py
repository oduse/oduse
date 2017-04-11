# -*- coding: utf-8 -*-
{
    'name': "至尚业务平台",
    'summary': u"""
        至尚业务平台。
        整合万嘉恒泰下属各个子系统的工作中心。""",
    'description': u"""
        至尚业务平台。
        整合万嘉恒泰下属各个子系统的工作中心。
    """,
    'author': u"至尚药业",
    'website': "http://www.zhishangyaoye.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'ZS',
    'version': '0.1',
    'application': True,
    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'purchase', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/product_zs_view.xml',
    ],
    'installable': True,
}