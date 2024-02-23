from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import User


# 定制User模型的管理界面
class UserAdmin(admin.ModelAdmin):
    # 在列表页显示的字段d
    list_display = ('username','role','department','email')
    # 设置可以通过搜索框搜索的字段
    search_fields = ('username', 'department','role')

    # 设置可以作为过滤条件的字段
    list_filter = ('username', 'department','role')


    # 设置每页显示的记录数量
    list_per_page = 25




# 用扩展后的UserAdmin重新注册User模型

admin.site.register(User, UserAdmin)
