{
    'name': 'Dayflow HR Extension',
    'version': '1.0',
    'summary': 'Custom HR dashboard extension for Dayflow HRMS',
    'category': 'Human Resources',
    'depends': ['hr', 'hr_attendance', 'hr_holidays'],
    'data': [
        'security/ir.model.access.csv',
        'views/dayflow_dashboard_views.xml',
        'data/demo_data.xml',
    ],
    'installable': True,
    'application': True,
}