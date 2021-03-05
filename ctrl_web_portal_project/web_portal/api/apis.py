from rest_framework import viewsets, status, response
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from web_portal.models.account_models import AccountModel
from web_portal.models.company_models import CompanyModel
from web_portal.serializers import (
    AccountModelSerializer,
    CompanyModelSerializer,
    CompanyDetailSerializer,
    AccountDetailSerializer,
)


class CompanyModelViewSet(APIView):
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
        except Snippet.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CompanyDetailSerializer(snippet)
        return Response(serializer.data)

    def post(self, request):
        company_data = CompanyModel.objects.all()
        serializer = CompanyModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountModelViewSet(APIView):
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


class AccountDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return AccountModel.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = AccountDetailSerializer(snippet)
        return Response(serializer.data)
