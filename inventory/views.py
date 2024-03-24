from .models import InventoryRecord
from .serializers import InventoryRecordSerializer
from rest_framework.generics import DestroyAPIView,UpdateAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from rest_framework.viewsets import GenericViewSet

# 查询所有盘点记录
class InventoryRecordView(ListModelMixin,GenericViewSet):
    queryset = InventoryRecord.objects.all()
    serializer_class = InventoryRecordSerializer

# 创建盘点记录
class InventoryRecordCreateView(GenericViewSet,CreateModelMixin):
    queryset = InventoryRecord.objects.all()
    serializer_class = InventoryRecordSerializer

# 根据id删除盘点记录
class InventoryRecordDeleteByIdView(DestroyAPIView):
    queryset = InventoryRecord.objects.all()
    serializer_class = InventoryRecordSerializer
    lookup_field='id'

# 根据id更新盘点记录
class InventoryRecordUpdateByIdView(UpdateAPIView):
    queryset = InventoryRecord.objects.all()
    serializer_class = InventoryRecordSerializer
    lookup_field='id'

