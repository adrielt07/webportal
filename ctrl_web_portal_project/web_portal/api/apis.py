from rest_framework import viewsets, status, response
from django_filters.rest_framework import DjangoFilterBackend
from web_portal.models.account_models import AccountModel
from web_portal.serializers import AccountModelSerializer


class AccountModelViewSet(viewsets.ViewSet):
    model = AccountModel
    queryset = AccountModel.objects.all()
    serializer_class = AccountModelSerializer
    filter_fields = ["id", "fistname", "lastname"]
