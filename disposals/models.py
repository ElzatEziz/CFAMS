from django.db import models
from assets.models import Asset  # 假设资产模型位于assets应用中
import uuid


class DisposalRecord(models.Model):
    """使用UUIDField作为主键，以保持ID的唯一性和复杂性。
    asset字段是一个外键，指向Asset模型，表示被处置的资产。
    DISPOSAL_METHOD_CHOICES为处置方法提供了预定义的选项，
    如销售、捐赠或报废等。此外，还包括了处置日期、接收方（如果适用）、以及与处置相关的成本或收入。
    """
    DISPOSAL_METHOD_CHOICES = (
        ('sale', '售出'),
        ('donation', '捐赠'),
        ('scrap', '废弃'),
        # 根据需要添加更多处置方式
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, verbose_name='处置资产')
    disposal_date = models.DateField(verbose_name='处置日期')
    disposal_method = models.CharField(max_length=50, choices=DISPOSAL_METHOD_CHOICES, verbose_name='处置方式')
    recipient = models.CharField(max_length=255, blank=True, null=True, verbose_name='接收方')
    cost_or_revenue = models.FloatField(verbose_name='相关成本或收入')

    def __str__(self):
        return f"{self.asset.name} - {self.disposal_method} - {self.disposal_date}"

    class Meta:
        verbose_name = '资产处置记录'
        verbose_name_plural = '资产处置记录'
