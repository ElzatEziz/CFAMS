from rest_framework import serializers

from .models import Asset

class AssetsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Asset
        fields = '__all__'
    def to_representation(self, instance):
        """
        将模型实例转换为用于序列化的数据格式。
        对于 asset_type 和 state 字段，返回它们的可读字符串。
        """
        ret = super().to_representation(instance)
        ret['asset_type'] = instance.get_asset_type_display()
        ret['state'] = instance.get_state_display()
        return ret