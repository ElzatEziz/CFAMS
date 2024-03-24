from django.db import models
from assets.models import Asset  # 假设资产模型位于assets应用中


class InventoryRecord(models.Model):
    """
    asset字段是一个外键，指向Asset模型，表示被盘点的资产。
    inventory_date、actual_location、status和inventory_personnel字段分别记录了盘点的日期、
    资产的实际位置、盘点时的状态以及进行盘点的人员。
    """
    INVENTORY_STATUES = (
    ('Good', '良好'),
    ('Damaged', '损坏'),
    ('Missing', '丢失'),
    ('Needs Repair', '待维修'),
    ('Scrapped', '报废'),
    ('In Stock', '在库'),
    ('Faulty', '故障'),
    ('Normal', '正常'),
)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, verbose_name='资产')
    inventory_date = models.DateField(verbose_name='盘点日期')
    actual_location = models.CharField(max_length=255, verbose_name='实际位置')
    status = models.CharField(max_length=50, choices=INVENTORY_STATUES,verbose_name='状态')
    inventory_personnel = models.CharField(max_length=255, verbose_name='盘点人员')

    def __str__(self):
        return f"{self.asset.name} - {self.inventory_date}"

    class Meta:
        db_table="tb_inventory"
        verbose_name = '盘点记录'
        verbose_name_plural = verbose_name
