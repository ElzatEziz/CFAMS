from django.contrib import admin
from .models import Asset


@admin.register(Asset)
# 定制Asset模型的管理界面
class AssetAdmin(admin.ModelAdmin):
    # 在列表页显示的字段d
    list_display = ('name', 'asset_type', 'purchase_date', 'cost', 'supplier_info', 'location', 'state')

    # 设置可以通过搜索框搜索的字段
    search_fields = ('name', 'supplier_info', 'location')

    # 设置可以作为过滤条件的字段
    list_filter = ('asset_type', 'state', 'purchase_date')

    # 设置在详情页分组显示的字段
    fieldsets = (
        ('基本信息', {'fields': ('name', 'asset_type', 'state')}),
        ('详细信息', {'fields': ('purchase_date', 'cost', 'supplier_info', 'location')}),
    )

    # 设置那些字段可以直接在列表页编辑
    list_editable = ('state',)

    # 设置每页显示的记录数量
    list_per_page = 25


admin.site.site_header = '校园固定资产管理系统'
admin.site.site_title = '校园固定资产管理系统'
