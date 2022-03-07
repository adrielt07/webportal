from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from web_portal.models.account_models import AccountModel


class UserlistView(View):
    def get(self, request):
        account_model = AccountModel.objects.filter(company_id=request.user.company_id)
        context = {
            'firstname': request.user.firstname,
            'lastname': request.user.lastname,
            'title': 'User list',
            'page_title': 'User list',
            'account_model': account_model,
        }
        return render(request, 'web_portal/userlist.html', {'context': context})


class UserDetailView(View):
    def get(self, request):
        """ Use to view more detail about the schedule """
        account = request.user
        context = {
            'firstname': request.user.firstname,
            'lastname': request.user.lastname,
            'title': 'Account Settings',
            'page_title': 'Account Settings',
        }
        return render(request, 'web_portal/userdetail.html', {'context': context, 'account': account})
