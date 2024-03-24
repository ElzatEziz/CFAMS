from rest_framework import serializers
from .models import InventoryRecord
from assets.models import Asset

class InventoryRecordSerializer(serializers.ModelSerializer):
    """盘点记录序列化器"""
    asset = serializers.PrimaryKeyRelatedField(queryset=Asset.objects.all(), label='盘点资产')
    asset_name = serializers.CharField(source='asset.name', read_only=True, label='资产名称')
    inventory_date = serializers.DateField(label='盘点日期')

    class Meta:
        model = InventoryRecord
        fields = '__all__'
