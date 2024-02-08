from django.contrib import admin
from .models import DisposalRecord


@admin.register(DisposalRecord)
# 定制DisposalRecord模型的管理界面
class DisposalRecordAdmin(admin.ModelAdmin):

    # 在列表页显示的字段
    list_display = ('asset', 'disposal_date', 'disposal_method', 'recipient', 'cost_or_revenue')

    # 设置可以通过搜索框搜索的字段
    search_fields = ('asset__name', 'recipient')

    # 设置可以作为过滤条件的字段
    list_filter = ('disposal_method', 'disposal_date')

    # 设置在详情页按分组显示的字段
    fieldsets = (
        ('基本信息', {'fields': ('asset', 'disposal_method', 'disposal_date')}),
        ('详细信息', {'fields': ('recipient', 'cost_or_revenue')}),
    )

    # 设置那些字段可以直接在列表页编辑
    list_editable = ('disposal_method', 'recipient')

    # 设置每页显示的记录数量
    list_per_page = 20


