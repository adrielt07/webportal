from rest_framework import viewsets, status, response, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.http import Http404
from web_portal.models.account_models import AccountModel
from web_portal.models.company_models import CompanyModel
from web_portal.models.location_models import LocationModel
from web_portal.serializers import (
    AccountModelSerializer,
    CompanyModelSerializer,
    CompanyDetailSerializer,
    AccountDetailSerializer,
    LocationModelSerializer,
)


class CompanyModelViewSet(APIView):
    #permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        company = CompanyModel.objects.all()
        serializer = CompanyModelSerializer(company, many=True)
        return Response(serializer.data)


    def post(self, request):
        user_accounts = CompanyModel.objects.all()
        serializer = CompanyModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyDetail(APIView):
    def get_object(self, pk):
        try:
            return CompanyModel.objects.get(pk=pk)
        except CompanyModel.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        company = self.get_object(pk)
        serializer = CompanyDetailSerializer(company)
        return Response(serializer.data)

    def post(self, request):
        company_data = CompanyModel.objects.all()
        serializer = CompanyModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateUserView(generics.CreateAPIView):
    """Api to create user"""
    serializer_class = AccountModelSerializer

class AccountModelViewSet(APIView):
    serializer_class = AccountModelSerializer
    def get(self, request, format=None):
        user_accounts = AccountModel.objects.all()
        serializer = AccountModelSerializer(user_accounts, many=True)
        return Response(serializer.data)


    def post(self, request):
        user_accounts = AccountModel.objects.all()
        serializer = AccountModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LocationModelViewSet(APIView):
    def get(self, request, format=None):
        locations = LocationModel.objects.all()
        serializer = LocationModelSerializer(locations, many=True)
        return Response(serializer.data)


class AccountDetail(APIView):
    """
    Retrieve, update or delete a account instance.
    """
    def get_object(self, pk):
        try:
            return AccountModel.objects.get(pk=pk)
        except AccountModel.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        account = self.get_object(pk)
        serializer = AccountDetailSerializer(account)
        return Response(serializer.data)


    def delete(self, request, pk, format=None):
        account = self.get_object(pk)
        user = request.user
        if user.id == account.id:
            return Response(status=status.HTTP_403_FORBIDDEN)

        if user.is_client_admin and user.company.id == user.company.id:
            account.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_403_FORBIDDEN)
