from django.contrib import admin
from django.urls import path
from web_portal.views.homepage_view import HomepageView

urlpatterns = [
    path('home/', HomepageView.as_view()),
]
