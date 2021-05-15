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
            'title': 'Ctrl-layer Portal Home',
            'page_title': 'User list',
            'account_model': account_model,
        }
        return render(request, 'web_portal/userlist.html', {'context': context})
