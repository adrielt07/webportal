from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from web_portal.api import apis

app_name = 'web_portal'

router = DefaultRouter()

#API Endpoints

urlpatterns = [
    path('', include(router.urls)),
    path('v1/', include(router.urls)),
    path('company/', apis.CompanyModelViewSet.as_view(), name='company'),
    path('company/<int:pk>', apis.CompanyDetail.as_view(), name='company_detail'),
    path('users/', apis.AccountModelViewSet.as_view(), name='users'),
    path('users/<int:pk>/', apis.AccountDetail.as_view(), name='users_detail'),
    path('locations/', apis.LocationModelViewSet.as_view(), name='locations'),
    path('create/', apis.CreateUserView.as_view(), name='create'),
]
