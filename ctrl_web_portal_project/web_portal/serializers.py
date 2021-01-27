from rest_framework import serializers, fields
from web_portal.models.account_models import AccountModel

class AccountModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AccountModel
        fields = ["id", "firstname", "lastname"]
        depth = 0
