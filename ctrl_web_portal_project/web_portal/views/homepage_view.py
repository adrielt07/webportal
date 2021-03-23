from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View


class HomepageView(View):
    def get(self, request):
        context = {
            'firstname': request.user.firstname,
            'lastname': request.user.lastname,
        }
        return render(request, 'web_portal/home.html', {'context': context})


class UserCreate(View):
    def get(self, request):
        return render(request, 'web_portal/signup.html')