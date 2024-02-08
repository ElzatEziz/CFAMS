from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import UserProfile


# 定制UserProfile模型的内联表单
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = '用户资料'
    fk_name = 'user'


# 扩展现有的User模型管理界面以包含UserProfile
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    list_display = (
    'username', 'email', 'first_name', 'last_name', 'is_staff', 'get_role', 'get_phone', 'get_department')

    def get_role(self, instance):
        return instance.profile.role

    get_role.short_description = '角色'

    def get_phone(self, instance):
        return instance.profile.phone if instance.profile.phone else '-'

    get_phone.short_description = '电话号码'

    def get_department(self, instance):
        return instance.profile.department if instance.profile.department else '-'

    get_department.short_description = '部门'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserAdmin, self).get_inline_instances(request, obj)


# 注销原有的User模型注册
admin.site.unregister(User)
# 用扩展后的UserAdmin重新注册User模型
admin.site.register(User, UserAdmin)
