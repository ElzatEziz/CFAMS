from django.contrib import admin
from .models import InventoryRecord


@admin.register(InventoryRecord)
# 定制InventoryRecord模型的管理界面
class InventoryRecordAdmin(admin.ModelAdmin):
    # 在列表页显示的字段
    list_display = ('asset', 'inventory_date', 'actual_location', 'status', 'inventory_personnel')

    # 设置可以通过搜索框搜索的字段
    search_fields = ('asset__name', 'actual_location', 'inventory_personnel')

    # 设置可以作为过滤条件的字段
    list_filter = ('status', 'inventory_date')

    # 定制在详情页的字段排列和分组
    fieldsets = (
        (None, {'fields': ('asset', 'inventory_date', 'status')}),
        ('详细信息', {'fields': ('actual_location', 'inventory_personnel'), 'classes': ('collapse',)}),
    )


    # 设置每页显示的记录数量
    list_per_page = 20
