from django.contrib import admin
from django.urls import path
from web_portal.views.mainpage_view import MainpageViews

urlpatterns = [
    path('portal/', MainpageViews.as_view()),
]
