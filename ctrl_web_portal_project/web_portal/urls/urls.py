from django.contrib import admin
from django.urls import path
from web_portal.views.homepage_view import HomepageView
from web_portal.views.signup import SignUp


urlpatterns = [
    path('home/', HomepageView.as_view()),
    path('signup/', SignUp.as_view()),
]
