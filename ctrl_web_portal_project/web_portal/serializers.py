from rest_framework import serializers, fields
from web_portal.models.account_models import AccountModel
from web_portal.models.company_models import CompanyModel
from web_portal.models.location_models import LocationModel


class CompanyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = ["id", "company_name", "phone"]
        depth = 0


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationModel
        fields = ["id", "name",]
        depth = 0


class AccountDetailSerializer(serializers.ModelSerializer):
    company = CompanyModelSerializer(read_only=True)
    class Meta:
        model = AccountModel
        fields = ["id", "firstname", "lastname", "email", "is_active", "company"]
        depth = 0


class AccountModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountModel
        fields = ["id", "firstname", "lastname", "company", "email", "is_active"]
        depth = 0


class CompanyDetailSerializer(serializers.ModelSerializer):
    users = AccountModelSerializer(many=True, read_only=True)
    #address = AddressSerializerList(read_only=True)
    class Meta:
        model = CompanyModel
        fields = [
            "id",
            "company_name",
            "phone",
            "created_at",
            "updated_at",
            "users",
            "address",
            "city",
            "state",
            "zip_code",
            "country"
        ]
        depth = 0
