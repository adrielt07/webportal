from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View


class HomepageView(View):
    def get(self, request):
        return render(request, 'web_portal/home.html')


class UserCreate(View):
    def get(self, request):
        return render(request, 'web_portal/signup.html')