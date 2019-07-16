# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2018-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Anusha P P(<https://www.cybrosys.com>)
#    you can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <https://www.gnu.org/licenses/>.
#
#############################################################################

{
    'name': "Sale Promotion",
    'version': '11.0.1.0.0',
    'summary': """Create Promotion Offers For Sales""",
    'description': """This Module Allows to Set  Promotion Offers On Products And Product Categories.""",
    'author': "Cybrosys Techno Solutions",
    'maintainer': 'Cybrosys Techno Solutions',
    'company': "Cybrosys Techno Solutions",
    'website': "https://www.cybrosys.com",
    'category': 'Sales',
    'depends': ['sale', 'account_invoicing'],
    'data': [
        'security/ir.model.access.csv',
        'views/promotion_product.xml',
        'views/sale_promotion_rule.xml',
        'views/sale_order.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
}


