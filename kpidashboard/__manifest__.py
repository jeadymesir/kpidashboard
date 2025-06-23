{
    'name': "KPI Dashboard",
    'version': '17.0.2.0.1',
    'category': 'Productivity',
    'summary': """Easily create dynamic dashboards with configurable blocks""",
    'description': """This KPI Dashboard module allows you to create dynamic dashboards with configurable blocks.
                        You can add, edit, and delete blocks, and customize their content based on your needs.""",
    'author': 'Poekie',
    'depends': ['web'],
    'data': [
        'security/ir.model.access.csv',
        'views/dashboard_views.xml',
        'views/dynamic_block_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'kpidashboard/static/src/css/**/*.css',
            'kpidashboard/static/src/scss/**/*.scss',
            'kpidashboard/static/src/js/**/*.js',
            'kpidashboard/static/src/xml/**/*.xml',
            'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css',
            'kpidashboard/static/lib/js/interactjs.js',
        ],
    },
    'license': "AGPL-3",
    'installable': True,
    'auto_install': False,
    'application': True,
}



