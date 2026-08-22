from odoo import models, fields, api

class DayflowDashboard(models.Model):
    _name = 'dayflow.dashboard'
    _description = 'Employee Attendance & Leave Summary'

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    attendance_status = fields.Char(string='Today Attendance')
    pending_leaves = fields.Integer(string='Pending Leave Requests')
    approved_leaves = fields.Integer(string='Approved Leaves This Month')

    def compute_summary(self):
        for record in self:
            # Get today's attendance for this employee
            attendance = self.env['hr.attendance'].search([
                ('employee_id', '=', record.employee_id.id)
            ], limit=1, order='check_in desc')
            record.attendance_status = 'Present' if attendance and not attendance.check_out else 'Not Checked In'

            # Count pending leave requests
            record.pending_leaves = self.env['hr.leave'].search_count([
                ('employee_id', '=', record.employee_id.id),
                ('state', '=', 'confirm')
            ])

            # Count approved leaves this month
            record.approved_leaves = self.env['hr.leave'].search_count([
                ('employee_id', '=', record.employee_id.id),
                ('state', '=', 'validate')
            ])