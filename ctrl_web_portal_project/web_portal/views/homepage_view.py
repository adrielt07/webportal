from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

class HomepageView(View):
    def get(self, request):
        # <view logic>
        #return HttpResponse('result')
        return render(request, 'web_portal/home.html')