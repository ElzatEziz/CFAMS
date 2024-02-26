from .models import Report
from .serializer import ReportSerializer
from rest_framework.generics import ListCreateAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from rest_framework.viewsets import GenericViewSet

# 获取所有报告
class ReportView(GenericViewSet,ListModelMixin):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

# 获取单个报告
class ReportDetailView(ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    lookup_field = 'id'  # 使用报告的ID作为查找字段
    # def get_queryset(self):
    #     return Report.objects.filter(id=self.kwargs['id'])

# 新增报告
class ReportCreateView(GenericViewSet,CreateModelMixin):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

# 删除报告
class ReportDeleteByIdView(DestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    lookup_field = 'id'  # 使用报告的ID作为查找字段

# 更新报告
class ReportUpdateByIdView(UpdateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    lookup_field = 'id'  # 使用报告的ID作为查找字段