from .serializers import UserSerializer
from .models import User
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,CreateModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import AllowAny
class UserView(GenericViewSet,ListModelMixin,RetrieveModelMixin,CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class RegisterView(GenericViewSet,CreateModelMixin,GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    def create(self, request, *args, **kwargs):
        # 获取用户输入的用户名和密码
        username = request.data.get('username', None)
        # 检查用户名是否已经存在
        if User.objects.filter(username=username).first():
            return Response({'error': '用户名已存在'}, status=status.HTTP_400_BAD_REQUEST)
        # 创建用户实例
        user = User.objects.create(username=username)
        # 使用set_password方法设置密码
        password = request.data.get('password', None)
        user.set_password(password)
        user.save()
        # 返回用户实例
        serializer = self.get_serializer(user)
        return Response(serializer.data,status=status.HTTP_201_CREATED)


class LoginView(TokenObtainPairView):
    # 指定serializer_class如果你需要自定义TokenObtainPairSerializer
    # serializer_class = MyCustomTokenObtainPairSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = TokenObtainPairSerializer(data=request.data)
        print("",request.user)
        if serializer.is_valid():
            # 如果用户名和密码验证成功，则返回access和refresh tokens
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        else:
            # 如果用户名或密码验证失败，则返回错误信息
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)