"""
URL configuration for CFAMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,re_path
from assets.views import AssetView
from users.views import UserView, LoginView, RegisterView
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router = routers.DefaultRouter()
router.register('assets',AssetView)
router.register('users',UserView)
# router.register('login',LoginView,basename='login')
router.register('register',RegisterView,basename='register')

urlpatterns = [
    # path("assets/",AssetView.as_view({"get":"list","post":"create"})),
    # re_path("assets/(?P<pk>\d+)",AssetView.as_view({"get":"retrieve","delete":"destroy","put":"update"}))
    path('login/',LoginView.as_view(),name='login'),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls
