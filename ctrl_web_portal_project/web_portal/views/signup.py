from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

class SignUp(View):
    def get(self, request):
        return render(request, 'web_portal/signup.html')
