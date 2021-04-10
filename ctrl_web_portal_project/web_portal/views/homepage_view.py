from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View


class HomepageView(View):
    def get(self, request):
        context = {
            'firstname': request.user.firstname,
            'lastname': request.user.lastname,
            'title': 'Ctrl-layer Portal Home'
        }
        return render(request, 'web_portal/home.html', {'context': context})
