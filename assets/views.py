from .models import Asset
from .serializers import AssetsSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin,CreateModelMixin,DestroyModelMixin,RetrieveModelMixin,UpdateModelMixin
import uuid
class AssetView(GenericViewSet,ListModelMixin,CreateModelMixin,DestroyModelMixin,RetrieveModelMixin,UpdateModelMixin):
    id = uuid.uuid1()
    queryset = Asset.objects.all()
    serializer_class = AssetsSerializer
