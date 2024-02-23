from django.db import models
from users.models import User

class Report(models.Model):
    """
    report_type字段用于指定报告的类型。
    created_at字段自动记录报告生成的时间。
    created_by字段记录报告的生成者，它是一个外键，指向Django内置的User模型。
    parameters字段可以用来存储生成报告所需的特定参数，例如报告的时间范围、特定的资产ID等，以JSON格式存储以保持灵活性。
    """
    REPORT_TYPE_CHOICES = (
        ('asset_summary', '资产摘要'),
        ('maintenance_history', '维护记录'),
        ('inventory_status', '库存状态'),
        ('disposal_record', '处置记录'),
        # 根据需要添加更多报告类型
    )
    title = models.CharField(max_length=100,verbose_name="标题",null=True)
    report_type = models.CharField(max_length=50, choices=REPORT_TYPE_CHOICES, verbose_name='报告类型')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='生成日期')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='生成者')
    parameters = models.TextField(verbose_name='报告参数', help_text='JSON格式的报告生成参数', blank=True, null=True)

    def __str__(self):
        return f"{self.get_report_type_display()} - {self.created_at.strftime('%Y-%m-%d')}"

    class Meta:
        db_table="tb_reports"
        verbose_name = '报告'
        verbose_name_plural = '报告'
