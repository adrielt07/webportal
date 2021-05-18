from django import forms
from django.db import models
from app_schedule.models import ScheduleModel


class CreateScheduleForm(forms.ModelForm):
    """ Define the required fields for adding a new company """
    schedule_date = models.DateTimeField(blank=True)

    class Meta:
        model = ScheduleModel
        fields = ["schedule_date"]
