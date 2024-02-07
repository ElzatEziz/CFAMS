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
