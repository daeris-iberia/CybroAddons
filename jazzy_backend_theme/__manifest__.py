# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2021-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

{
    "name": "Jazzy Backend Theme v15",
    "description": """Minimalist and elegant backend theme for Odoo 15, Backend Theme, Theme""",
    "summary": "Jazzy backed Theme V15 is an attractive theme for backend",
    "category": "Website",
    "version": "1.1",
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    "depends": ['base','web','mail','contacts','utm','sale','account','stock','purchase','calendar','crm','note','website','point_of_sale','mrp','repair','mass_mailing','mass_mailing_sms','project','survey','hr','hr_recruitment','hr_attendance','hr_holidays','hr_expense','maintenance','im_livechat','lunch','fleet','hr_timesheet','event','website_slides','membership','dp_eu_gdpr','daeris_support','hr_payroll','daeris_appointment'],#,'hr_custody','om_hr_payroll','hr_resignation','hr_payroll_community','hrms_dashboard','ohrms_overtime','hr_employee_shift','hr_reminder','hr_employee_transfer','hr_reward_warning'
    "data": [
        'views/style.xml',
        'views/res_config_settings.xml',
        'views/icons.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'jazzy_backend_theme/static/src/layout/style/layout_colors_frontend.scss',
            'jazzy_backend_theme/static/src/layout/style/layout_style_frontend.scss',
        ],
        'web.assets_backend': [
                'jazzy_backend_theme/static/src/layout/style/login.scss',
                'jazzy_backend_theme/static/src/layout/style/layout_colors.scss',
                'jazzy_backend_theme/static/src/components/app_menu/menu_order.css',
                'jazzy_backend_theme/static/src/layout/style/layout_style.scss',
                'jazzy_backend_theme/static/src/layout/style/sidebar.scss',
                'jazzy_backend_theme/static/src/components/app_menu/search_apps.js',
        ],
        'web.assets_qweb': [
                'jazzy_backend_theme/static/src/components/app_menu/side_menu.xml',
                'jazzy_backend_theme/static/src/xml/styles.xml',
        ],
    },
    'images': [
        'static/description/banner.png',
        'static/description/theme_screenshot.png',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
