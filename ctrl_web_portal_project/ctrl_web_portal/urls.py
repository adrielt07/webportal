"""ctrl_web_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import ctrl_web_portal.views as mainview

urlpatterns = [
    path('admin/', admin.site.urls),

    # web_portal urls
    path('', include('web_portal.urls.urls')),

    # Api urls
    path(r'api/', include('web_portal.urls.urls_api', namespace='api')),
    path(r'api/', include('web_portal.urls.urls_api', namespace='api_v1')),
]
