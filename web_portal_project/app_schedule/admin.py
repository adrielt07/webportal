from django.contrib import admin
from app_schedule.models import ScheduleModel

# Register your models here.
class ScheduleModelAdmin(admin.ModelAdmin):
    list_display = ("id", "company", "user")

admin.site.register(ScheduleModel, ScheduleModelAdmin)
