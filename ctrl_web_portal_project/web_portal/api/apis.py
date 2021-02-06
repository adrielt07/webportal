from rest_framework import viewsets, status, response
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from web_portal.models.account_models import AccountModel
from web_portal.models.company_models import CompanyModel
from web_portal.serializers import (
    AccountModelSerializer,
    CompanyModelSerializer,
)


class CompanyModelViewSet(APIView):
    def get(self, request, format=None):
        company = CompanyModel.objects.all()
        serializer = CompanyModelSerializer(company, many=True)
        return Response(serializer.data)


class AccountModelViewSet(APIView):
    def get(self, request, format=None):
        user_accounts = AccountModel.objects.all()
        serializer = AccountModelSerializer(user_accounts, many=True)
        return Response(serializer.data)

    def post(self, request):
        user_accounts = AccountModel.objects.all()
        serializer = AccountModelSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
