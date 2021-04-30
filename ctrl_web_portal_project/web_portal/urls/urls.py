from django.contrib import admin
from django.urls import path
from web_portal.views.homepage_view import HomepageView
from web_portal.views.signup_view import SignupView
from web_portal.views.auth_view import LoginpageView, RegisterPage, logout
from web_portal.views.create_company_view import CreateCompanyView
from web_portal.views.generic_view import GenericpageView
from web_portal.views.userlist_view import UserlistView

urlpatterns = [
    path('', HomepageView.as_view(), name="default_page"),
    path('home/', HomepageView.as_view(), name="home"),
    path('register/', SignupView.as_view(), name="signup"),
    path('company/add/', CreateCompanyView.as_view(), name="create_company"),
    path('login/', LoginpageView.as_view(), name="login"),
    path('generic/', GenericpageView.as_view(), name="generic"),
    path('users/', UserlistView.as_view(), name="userslist"),
    path('logout/', logout, name='logout'),
]
