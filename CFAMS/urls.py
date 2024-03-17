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
# from django.contrib import admin
from assets.views import AssetView
from users.views import UserView, LoginView, RegisterView,CurrentUserView
from assets.views import AssetCreateView,AssetDeleteByIdView,AssetUpdateByIdView,AssetFilterView
from reports.views import ReportView,ReportCreateView,ReportDeleteByIdView,ReportUpdateByIdView
from rest_framework import routers
from disposals.views import DisposalRecordView,DisposalRecordCreateView,DisposalRecordDeleteByIdView,DisposalRecordUpdateByIdView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router = routers.DefaultRouter()
router.register('assets',AssetView)
router.register('users',UserView)
router.register('register',RegisterView,basename='register')
router.register('current_user',CurrentUserView,basename='current_user')
router.register('assets_create',AssetCreateView,basename='assets_create')
router.register('assets_filter',AssetFilterView,basename='assets_filter')
router.register('reports',ReportView)
router.register('reports_create',ReportCreateView,basename='reports_create')
router.register('disposals',DisposalRecordView)
router.register('disposals_create',DisposalRecordCreateView,basename='disposals_create')

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/',LoginView.as_view(),name='login'),
    path('assets_delete/<int:id>/', AssetDeleteByIdView.as_view(), name='delete-asset'),
    path('assets_update/<int:id>/', AssetUpdateByIdView.as_view(), name='update-asset'),
    # path('assets_filter/', AssetFilterView.as_view({'get': 'list'}), name='filter-asset'),
    path('reports_delete/<int:id>/', ReportDeleteByIdView.as_view(), name='delete-report'),
    path('reports_update/<int:id>/', ReportUpdateByIdView.as_view(), name='update-report'),
    path('disposals_delete/<int:id>/', DisposalRecordDeleteByIdView.as_view(), name='delete-disposal'),
    path('disposals_update/<int:id>/', DisposalRecordUpdateByIdView.as_view(), name='update-disposal'),
]

urlpatterns += router.urls
