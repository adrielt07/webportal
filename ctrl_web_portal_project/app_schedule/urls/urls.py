from django.contrib import admin
from django.urls import path
from app_schedule.views import ScheduleView, CreateScheduleView

urlpatterns = [
    path('schedule/', ScheduleView.as_view(), name="list_schedule"),
    path('schedule/create', CreateScheduleView.as_view(), name="create_schedule"),
]
