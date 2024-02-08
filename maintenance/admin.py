from django.contrib import admin
from .models import MaintenanceRecord


@admin.register(MaintenanceRecord)
# 定制MaintenanceRecord模型的管理界面
class MaintenanceRecordAdmin(admin.ModelAdmin):
    # 在列表页显示的字段
    list_display = ('asset', 'maintenance_date', 'maintenance_type', 'cost', 'result')

    # 设置可以通过搜索框搜索的字段
    search_fields = ('asset__name', 'maintenance_type', 'result')

    # 设置可以作为过滤条件的字段
    list_filter = ('maintenance_type', 'maintenance_date')

    # 设置在详情页的字段排列和分组
    fieldsets = (
        (None, {'fields': ('asset', 'maintenance_date', 'maintenance_type')}),
        ('成本和结果', {'fields': ('cost', 'result'), 'classes': ('collapse',)}),
    )
    # 设置每页显示的记录数量
    list_per_page = 20

