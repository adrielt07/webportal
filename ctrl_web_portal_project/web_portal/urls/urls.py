from django.contrib import admin
from django.urls import path
from web_portal.views.homepage_view import HomepageView
from web_portal.views.signup_view import SignupView
from web_portal.views.auth_view import LoginpageView, RegisterPage, logout
from web_portal.views.generic_view import GenericpageView
from web_portal.views.user_view import UserlistView, UserDetailView
from web_portal.views import company_view

urlpatterns = [
    path('', HomepageView.as_view(), name="default_page"),
    path('home/', HomepageView.as_view(), name="home"),
    path('register/', SignupView.as_view(), name="create_user"),
    path('company/add/', company_view.CreateCompanyView.as_view(), name="create_company"),
    path('company/list/', company_view.ListCompanyView.as_view(), name="list_company"),
    path('company/<int:company_pk>/', company_view.CompanyDetailedView.as_view(), name="detail_company"),
    path('login/', LoginpageView.as_view(), name="login"),
    path('generic/', GenericpageView.as_view(), name="generic"),
    path('users/', UserlistView.as_view(), name="userslist"),
    path('users/detail', UserDetailView.as_view(), name="userdetail"),
    path('logout/', logout, name='logout'),
]
