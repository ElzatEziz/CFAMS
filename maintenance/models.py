from django.db import models
from assets.models import Asset  # 假设资产模型位于assets应用中


class MaintenanceRecord(models.Model):
    """
    定义了MaintenanceRecord模型，其中asset字段是一个外键，指向Asset模型，
    表示这条维护记录关联的资产。MAINTENANCE_TYPE_CHOICES为维护类型提供了预定义的选项。
    模型的每个字段都设置了verbose_name，以便在Django管理界面中显示更友好的字段名称。
    """
    MAINTENANCE_TYPE_CHOICES = (
        ('routine_check', '例行检查'),
        ('emergency_repair', '紧急维修'),
        ('part_replacement', '零件更换'),
        # 根据需要添加更多维护类型
    )
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, verbose_name='关联资产')
    maintenance_date = models.DateField(verbose_name='维护日期')
    maintenance_type = models.CharField(max_length=50, choices=MAINTENANCE_TYPE_CHOICES, verbose_name='维护类型')
    cost = models.FloatField(verbose_name='成本')
    result = models.TextField(verbose_name='结果')
    notes = models.TextField(blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return f"{self.asset.name} - {self.maintenance_date}"

    class Meta:
        db_table="tb_maintenance"
        verbose_name = '维护记录'
        verbose_name_plural = '维护记录'
