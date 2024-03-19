from .models import Asset
from .serializers import AssetsSerializer
from rest_framework.request import HttpRequest
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import DestroyAPIView,UpdateAPIView, ListAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from rest_framework.response import Response
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

# 筛选资产类型和状态
class AssetFilterView(GenericViewSet,ListModelMixin):
    queryset = Asset.objects.all()
    serializer_class = AssetsSerializer
    def get_queryset(self):
        asset_type=self.request.GET.get('asset_type')
        state=self.request.GET.get('state')
        print(asset_type)
        queryset = Asset.objects.all()
        if asset_type:
            queryset = queryset.filter(asset_type=asset_type)
        if state:
            queryset = queryset.filter(state=state)
        return queryset

