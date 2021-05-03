from django.contrib import admin
from django.urls import path
from schedule.views import ScheduleView

urlpatterns = [
    path('schedule/', ScheduleView.as_view(), name="schedule"),
]
