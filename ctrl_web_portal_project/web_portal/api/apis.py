from rest_framework import viewsets, status, response
from django_filters.rest_framework import DjangoFilterBackend
from web_portal.models.account_models import AccountModel
from web_portal.models.company_models import CompanyModel
from web_portal.serializers import (
    AccountModelSerializer,
    CompanyModelSerializer,
)


class CompanyModelViewSet(viewsets.ModelViewSet):
    model = CompanyModel
    queryset = CompanyModel.objects.all()
    serializer_class = CompanyModelSerializer
    filter_fields = ["company_name", "phone", "id"]


class AccountModelViewSet(viewsets.ModelViewSet):
    model = AccountModel
    queryset = AccountModel.objects.all()
    serializer_class = AccountModelSerializer
    filter_fields = ["id", "fistname", "lastname", "company"]
