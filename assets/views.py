from .models import Asset
from .serializers import AssetsSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import DestroyAPIView,UpdateAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin
import uuid


class AssetView(GenericViewSet,ListModelMixin):
    id = uuid.uuid1()
    queryset = Asset.objects.all()
    serializer_class = AssetsSerializer

# 新增资产
class AssetCreateView(GenericViewSet,CreateModelMixin):
    queryset = Asset.objects.all()
    serializer_class = AssetsSerializer

# 根据id删除资产
class AssetDeleteByIdView(DestroyAPIView):
    # 从请求中获取id并删除aaset_type
    queryset = Asset.objects.all()
    serializer_class = AssetsSerializer
    lookup_field = 'id'  # 使用资产的ID作为查找字段

# 更新资产
class AssetUpdateByIdView(UpdateAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetsSerializer
    lookup_field = 'id'  # 使用资产的ID作为查找字段