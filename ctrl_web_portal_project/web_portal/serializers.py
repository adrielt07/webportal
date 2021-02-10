from rest_framework import serializers, fields
from web_portal.models.account_models import AccountModel
from web_portal.models.company_models import CompanyModel
from web_portal.models.location_models import AddressModel


class CompanyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = ["id", "company_name", "phone"]
        depth = 0


class AccountModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountModel
        fields = ["id", "firstname", "lastname", "company"]
        depth = 0


class AddressSerializerList(serializers.ModelSerializer):
    class Meta:
        model = AddressModel
        fields = ["id", "street_address", "state", "country", "zip_code", "created_at", "updated_at"]
        depth = 0


class AccountDetailSerializer(serializers.ModelSerializer):
    company = CompanyModelSerializer(read_only=True)
    class Meta:
        model = AccountModel
        fields = ["id", "firstname", "lastname", "company"]
        depth = 0


class CompanyDetailSerializer(serializers.ModelSerializer):
    users = AccountModelSerializer(many=True, read_only=True)
    address = AddressSerializerList(read_only=True)
    #print(users)
    class Meta:
        model = CompanyModel
        fields = ["id", "company_name", "phone", "created_at", "updated_at", "address", "users"]
        depth = 0
