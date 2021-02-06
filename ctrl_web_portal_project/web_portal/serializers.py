from rest_framework import serializers, fields
from web_portal.models.account_models import AccountModel
from web_portal.models.company_models import CompanyModel


class CompanyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = ["company_name", "phone", "id"]
        depth = 0


class AccountModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountModel
        fields = ["id", "firstname", "lastname", "company"]
        depth = 0
