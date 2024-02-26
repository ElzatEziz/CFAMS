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
from rest_framework.views import APIView
# 获取所有用户
class UserView(GenericViewSet,ListModelMixin,RetrieveModelMixin,CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
# 注册新用户
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

# 登录用户并返回Token
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
        


# 获取当前登录用户信息
class CurrentUserView(ListModelMixin,GenericViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        """
        仅返回当前登录用户的查询集。
        """
        # self.request.user 是当前通过JWT认证的用户
        # 我们通过filter返回一个只包含当前用户的查询集
        return User.objects.filter(id=self.request.user.id)

    def list(self, request, *args, **kwargs):
        """
        重写list方法以改变默认行为，确保即使是列表视图也只返回当前用户。
        """
        # 这里调用ListModelMixin的list方法，它会使用get_queryset的结果
        return super().list(request, *args, **kwargs)