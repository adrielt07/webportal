from urllib import parse
from rest_framework import viewsets, status, response, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from django.http import Http404, JsonResponse
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
import json


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

    
    def patch(self, request, pk):
        user = request.user.id
        payload = json.loads(request.body)
        company_item = CompanyModel.objects.filter(id=pk)
        company_item.update(**payload)
        company = CompanyModel.objects.get(id=pk)
        serializer = CompanyModelSerializer(company)
        return JsonResponse({'company': serializer.data}, safe=False, status=status.HTTP_200_OK)


class CreateUserView(generics.CreateAPIView):
    """Api to create user"""
    serializer_class = AccountModelSerializer


class AccountModelViewSet(APIView, PageNumberPagination):
    serializer_class = AccountModelSerializer     
    page_size = 10
    max_page_size = 10

    def get_queryset(self):
        filter_data = {key: value for key, value in self.query.items()}
        user_accounts = AccountModel.objects.filter(**filter_data)
        return self.paginate_queryset(user_accounts, self.request)


    def get(self, request):
        self.query = request.query_params
        user_accounts = self.get_queryset()
        serializer = AccountModelSerializer(user_accounts, many=True)
        return self.get_paginated_response(serializer.data)


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


    def patch(self, request, pk):
        user = request.user.id
        payload = json.loads(request.body)
        account_item = AccountModel.objects.filter(id=pk)
        account_item.update(**payload)
        account = AccountModel.objects.get(id=pk)
        serializer = AccountModelSerializer(account)
        return JsonResponse({'account': serializer.data}, safe=False, status=status.HTTP_200_OK)
