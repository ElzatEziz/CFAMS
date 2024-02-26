from rest_framework import serializers
from .models import DisposalRecord
from assets.models import Asset

class DisposalRecordSerializer(serializers.ModelSerializer):
    """处置记录序列化器"""
    asset = serializers.PrimaryKeyRelatedField(queryset=Asset.objects.all(), label='处置资产')
    asset_name = serializers.CharField(source='asset.name', read_only=True, label='资产名称')
    disposal_method = serializers.CharField(source='get_disposal_method_display', read_only=True, label='处置方式')

    class Meta:
        model = DisposalRecord
        fields = '__all__'
        extra_kwargs = {
            'disposal_date': {'label': '处置日期'},
            'recipient': {'label': '接收方'},
            'cost_or_revenue': {'label': '相关成本或收入'}
        }