from django.contrib import admin
from django.urls import path
from app_schedule.views import ScheduleView

urlpatterns = [
    path('schedule/', ScheduleView.as_view(), name="schedule"),
]
