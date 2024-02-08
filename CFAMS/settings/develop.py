from .base import *  # NOQA

# 在开发环境开启DEBUG正常，但是在线上环境开启这个就是灾难
DEBUG = True
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "cfams",
        "USER": "root",
        "PASSWORD": "azez110311",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "cfams_static/"
STATIC_ROOT = "static"
STATICFILES_DIR = [
    os.path.join(BASE_DIR, "static"),
]

# SimpleUi配置
SIMPLEUI_HOME_TITLE = '校园固定资产管理系统'
SIMPLEUI_LOGIN_TITLE = '校园固定资产管理系统'
SIMPLEUI_HOME_INFO = False
SIMPLEUI_ANALYSIS = False
SIMPLEUI_DEFAULT_THEME = 'layui.css'

SIMPLEUI_CONFIG = {
    'system_keep': False,
    'menus': [
        {
            'name': '固定资产',
            'icon': 'fa fa-th-list',
            'models': [
                {
                    'name': '资产',
                    # 注意url按'/admin/应用名小写/模型名小写/'命名。
                    'url': '/admin/assets/asset/',
                    'icon': 'fa fa-tasks'
                },
            ]
        },
        {
            'name': '资产处置',
            'icon': 'fa-solid fa-chart-simple',
            'models': [
                {
                    'name': '处置记录',
                    # 注意url按'/admin/应用名小写/模型名小写/'命名。
                    'url': '/admin/disposals/disposalrecord/',
                    'icon': 'fa-solid fa-chart-simple'
                },
            ]
        },
        {
            'name': '资产盘点',
            'icon': 'fa-solid fa-clipboard',
            'models': [
                {
                    'name': '盘点记录',
                    # 注意url按'/admin/应用名小写/模型名小写/'命名。
                    'url': '/inventory/inventoryrecord/',
                    'icon': 'fa-regular fa-clipboard'
                },
            ]
        },
        {
            'name': '资产维护',
            'icon': 'fa-solid fa-gear',
            'models': [
                {
                    'name': '维护记录',
                    # 注意url按'/admin/应用名小写/模型名小写/'命名。
                    'url': '/admin/maintenance/maintenancerecord/',
                    'icon': 'fa-regular fa-gear'
                },
            ]
        },
        {
            'name': '资产记录',
            'icon': 'fa-solid fa-book',
            'models': [
                {
                    'name': '报告',
                    # 注意url按'/admin/应用名小写/模型名小写/'命名。
                    'url': '/admin/reports/report/',
                    'icon': 'fa-regular fa-book'
                },
            ]
        },
        {
            'app': 'auth',
            'name': '权限认证',
            'icon': 'fas fa-user-shield',
            'models': [
                {
                    'name': '用户列表',
                    'icon': 'fa fa-user',
                    'url': 'auth/user/'
                },
                {
                    'name': '用户组',
                    'icon': 'fa fa-th-list',
                    'url': 'auth/group/'
                }
            ]
        },
    ]
}

# 隐藏首页的快捷操作和最近动作
SIMPLEUI_HOME_QUICK = False
SIMPLEUI_HOME_ACTION = False
