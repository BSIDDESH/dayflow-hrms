from odoo import models, fields


class DayflowDashboard(models.Model):
    _name = "dayflow.dashboard"
    _description = "Dayflow HR Dashboard"

    name = fields.Char(string="Name", required=True)
    employee_count = fields.Integer(string="Employees", default=0)
    present_count = fields.Integer(string="Present", default=0)
    absent_count = fields.Integer(string="Absent", default=0)
    leave_count = fields.Integer(string="On Leave", default=0)