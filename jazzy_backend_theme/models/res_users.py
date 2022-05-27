# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, modules


class Users(models.Model):
    _name = 'res.users'
    _inherit = ['res.users']

    @api.model
    def systray_get_activities(self):
        """ Update the systray icon to use the
        custom one instead of standard icon. """
        activities = super(Users, self).systray_get_activities()
        for activity in activities:
            if activity['model'] == 'res.partner':
                activity['icon'] = '/jazzy_backend_theme/static/src/img/icons/Contacts.svg'
            elif activity['model'] == 'note.note':
                activity['icon'] = '/jazzy_backend_theme/static/src/img/icons/Note.svg'
            elif activity['model'] == 'crm.lead':
                activity['icon'] = '/jazzy_backend_theme/static/src/img/icons/CRM.svg'
            elif activity['model'] == 'mailing.mailing':
                activity['icon'] = '/jazzy_backend_theme/static/src/img/icons/EmailMarketing.svg'
            elif activity['model'] == 'calendar.event':
                activity['icon'] = '/jazzy_backend_theme/static/src/img/icons/Calendar.svg'
            elif activity['model'] == 'product.template':
                activity['icon'] = '/jazzy_backend_theme/static/src/img/icons/Inventory.svg'
            elif activity['model'] == 'fleet.vehicle.log.contract':
                activity['icon'] = '/jazzy_backend_theme/static/src/img/icons/Fleet.svg'
            elif activity['model'] == 'fleet.vehicle':
                activity['icon'] = '/jazzy_backend_theme/static/src/img/icons/Fleet.svg'
            elif activity['model'] == 'hr.employee':
                activity['icon'] = '/jazzy_backend_theme/static/src/img/icons/Employees.svg'
            elif activity['model'] == 'hr.contract':
                activity['icon'] = '/jazzy_backend_theme/static/src/img/icons/Employees.svg'
            elif activity['model'] == 'hr.expense':
                activity['icon'] = '/jazzy_backend_theme/static/src/img/icons/Expenses.svg'
            elif activity['model'] == 'hr.expense.sheet':
                activity['icon'] = '/jazzy_backend_theme/static/src/img/icons/Expenses.svg'
            elif activity['model'] == 'hr.leave.allocation':
                activity['icon'] = '/jazzy_backend_theme/static/src/img/icons/TimeOff.svg'
            elif activity['model'] == 'hr.leave':
                activity['icon'] = '/jazzy_backend_theme/static/src/img/icons/TimeOff.svg'
            elif activity['model'] == 'hr.applicant':
                activity['icon'] = '/jazzy_backend_theme/static/src/img/icons/Recruitment.svg'
            elif activity['model'] == 'product.product':
                activity['icon'] = '/jazzy_backend_theme/static/src/img/icons/Inventory.svg'
            elif activity['model'] == 'project.task':
                activity['icon'] = '/jazzy_backend_theme/static/src/img/icons/Project.svg'
            elif activity['model'] == 'purchase.order':
                activity['icon'] = '/jazzy_backend_theme/static/src/img/icons/Purchase.svg'
            elif activity['model'] == 'sale.order':
                activity['icon'] = '/jazzy_backend_theme/static/src/img/icons/Sales.svg'
            elif activity['model'] == 'daeris.support.ticket':
                activity['icon'] = '/jazzy_backend_theme/static/src/img/icons/Support.svg'
            elif activity['model'] == 'event.event':
                activity['icon'] = '/jazzy_backend_theme/static/src/img/icons/Events.svg'
            elif activity['model'] == 'account.move':
                activity['icon'] = '/jazzy_backend_theme/static/src/img/icons/Invoicing.svg'
            else:
                continue
        return activities
