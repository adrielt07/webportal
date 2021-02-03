from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from web_portal.api import apis

app_name = 'api'

router = DefaultRouter()

#API Endpoints
router.register(r'accounts', apis.AccountModelViewSet, 'accounts')
router.register(r'company', apis.CompanyModelViewSet, 'company')


urlpatterns = [
    path('', include(router.urls)),
    path('v1/', include(router.urls)),
]
