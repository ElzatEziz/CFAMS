import uuid

from django.db import models


class Asset(models.Model):
    """
    定义了Asset模型，其中包含了之前讨论的所有字段。TYPE_CHOICES和STATE_CHOICES为资产类型和状态提供了预定义的选项。
    """
    TYPE_CHOICES = (
        ('computer', '计算机'),
        ('furniture', '家具'),
        ('equipment', '设备'),
        # 可根据需要添加更多资产类型
    )
    STATE_CHOICES = (
        ('in_use', '使用中'),
        ('maintenance', '维护中'),
        ('disposed', '处置中'),
        # 可根据需要添加更多状态选项
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name='资产名称')
    asset_type = models.CharField(max_length=50, choices=TYPE_CHOICES, verbose_name='资产类型')
    purchase_date = models.DateField(verbose_name='购买日期')
    cost = models.FloatField(verbose_name='成本')
    supplier_info = models.CharField(max_length=255, verbose_name='供应商信息')
    location = models.CharField(max_length=255, verbose_name='存放位置')
    state = models.CharField(max_length=50, choices=STATE_CHOICES, verbose_name='状态')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '资产'
        verbose_name_plural = '资产'
