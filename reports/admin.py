from django.contrib import admin
from django.contrib.auth.models import User
from .models import Report


@admin.register(Report)
# 定制Report模型的管理界面
class ReportAdmin(admin.ModelAdmin):
    # 在列表页显示的字段
    list_display = ('title', 'report_type', 'created_at', 'created_by_display', 'parameters')

    # 设置可以通过搜索框搜索的字段
    search_fields = ('title', 'parameters')

    # 设置可以作为过滤条件的字段
    list_filter = ('report_type', 'created_at')

    # 只读字段设置
    readonly_fields = ('id', 'created_at', 'created_by')

    # 自定义字段展示
    def created_by_display(self, obj):
        return obj.created_by.username if obj.created_by else '-'

    created_by_display.short_description = '生成者'

    # 定制在详情页的字段排列和分组
    fieldsets = (
        (None, {'fields': ('id', 'title', 'report_type')}),
        ('报告详情', {'fields': ('created_at', 'created_by', 'parameters'), 'classes': ('collapse',)}),
    )

    # 设置每页显示的记录数量
    list_per_page = 20

    # 保存模型时，自动设置'created_by'字段为当前用户（如果是新建报告）
    def save_model(self, request, obj, form, change):
        if not change:  # 新建报告
            obj.created_by = request.user
        super().save_model(request, obj, form, change)



