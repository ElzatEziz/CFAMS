from .models import DisposalRecord
from .serializers import DisposalRecordSerializer
from rest_framework.generics import DestroyAPIView,UpdateAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin,ListModelMixin
from assets.models import Asset

# 查询所有处置记录
class DisposalRecordView(GenericViewSet, ListModelMixin):
    # 查询资产状态为处置中的资产
    queryset = DisposalRecord.objects.all()
    serializer_class = DisposalRecordSerializer

# 新增处置记录
class DisposalRecordCreateView(GenericViewSet,CreateModelMixin):
    # 新增资产状态而处置中的资产
    queryset = DisposalRecord.objects.all()
    serializer_class = DisposalRecordSerializer

# 根据id删除处置记录
class DisposalRecordDeleteByIdView(DestroyAPIView):
    queryset = DisposalRecord.objects.all()
    serializer_class = DisposalRecordSerializer
    lookup_field = 'id'  # 使用处置记录的ID作为查找字段

# 更新处置记录
class DisposalRecordUpdateByIdView(UpdateAPIView):
    queryset = DisposalRecord.objects.all()
    serializer_class = DisposalRecordSerializer
    lookup_field = 'id'  # 使用处置记录的ID作为查找字段
    




