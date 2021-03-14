from django.contrib.auth import get_user_model
from rest_framework import serializers, fields
from web_portal.models.account_models import AccountModel
from web_portal.models.company_models import CompanyModel
from web_portal.models.location_models import LocationModel


class CompanyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = ("id", "company_name", "phone", "address", "city", "zip_code",  "locations",)
        depth = 0


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationModel
        fields = ["id", "name",]
        depth = 0


class AccountDetailSerializer(serializers.ModelSerializer):
    company = CompanyModelSerializer(read_only=True)
    class Meta:
        model = get_user_model()
        fields = ("id", "firstname", "lastname", "email", "is_active", "company")
        depth = 0


class AccountModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "firstname", "lastname", "company", "email", "password", "is_active")
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}
        depth = 0

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)


class CompanyDetailSerializer(serializers.ModelSerializer):
    users = AccountModelSerializer(many=True, read_only=True)
    #address = AddressSerializerList(read_only=True)
    class Meta:
        model = CompanyModel
        fields = (
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
            "country",
            "locations"
        )
        depth = 0


class LocationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationModel
        fields = [
            "id",
            "name",
            "address",
            "city",
            "zip_code",
            "state",
            "country",
            "company"
        ]
        depth = 0