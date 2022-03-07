from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View


class HomepageView(View):
    def get(self, request):
        context = {
            'firstname': request.user.firstname,
            'lastname': request.user.lastname,
            'title': request.user.company.company_name,
            'is_super_admin': request.user.is_super_admin,
        }
        return render(
            request,
            'web_portal/home.html', {
                'context': context,
                'company': request.user.company,
                }
            )
