
from django.db import models


class Asset(models.Model):
    """
    定义了Asset模型，其中包含了之前讨论的所有字段。TYPE_CHOICES和STATE_CHOICES为资产类型和状态提供了预定义的选项。
    """
    TYPE_CHOICES = (
        ('computer', '计算机'),
        ('furniture', '家具'),
        ('equipment', '设备'),
        ('physical_education','体育设备'),
        ('electronics', '电子设备'),
        ('books_and_materials', '图书资料'),
        ('office_equipment', '办公设备'),
        ('art_and_decorations', '艺术品和装饰'),
        ('vehicles', '交通工具'),
        ('research_equipment', '科研设备'),
        ('security_equipment', '安全设备'),
        ('it_infrastructure', 'IT基础设施'),
        ('laboratory_equipment', '实验室设备'),
        ('musical_instruments', '乐器'),
        ('audio_visual_equipment', '音视频设备'),
        ('library_collections', '图书馆藏书'),
        ('teaching_aids', '教学辅助材料'),
        ('computer_lab_equipment', '计算机实验室设备'),
        ('medical_equipment', '医疗设备'),
        ('campus_infrastructure', '校园基础设施'),
        ('land_and_buildings', '土地和建筑物'),
        ('horticultural_assets', '园艺资产'),
        ('canteen_equipment', '食堂设备'),
        ('dormitory_furnishings', '宿舍家具'),
        ('workshop_machinery', '车间机械'),
        ('sporting_facilities', '体育设施'),
        ('sanitation_facilities', '卫生设施'),
        ('energy_and_utilities', '能源及公用设施'),
    )
    STATE_CHOICES = (
        ('in_use', '使用中'),
        ('maintenance', '维护中'),
        ('disposed', '处置中'),
        # 可根据需要添加更多状态选项
    )
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
        db_table="tb_assets"
        verbose_name = '资产'
        verbose_name_plural = verbose_name
