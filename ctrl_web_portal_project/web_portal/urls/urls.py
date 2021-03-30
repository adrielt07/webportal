from django.contrib import admin
from django.urls import path
from web_portal.views.homepage_view import HomepageView
from web_portal.views.auth_view import LoginpageView, RegisterPage, logout
from web_portal.views.generic_view import GenericpageView
from web_portal.views.signup import SignUp


urlpatterns = [
    path('', HomepageView.as_view(), name="default_page"),
    path('home/', HomepageView.as_view(), name="home"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('login/', LoginpageView.as_view(), name="login"),
    path('generic/', GenericpageView.as_view(), name="generic"),
    path('register/', RegisterPage, name="register"),
    path('logout/', logout, name='logout'),
]
