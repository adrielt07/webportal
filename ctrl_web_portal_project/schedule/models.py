from django.db import models

# Create your models here.
class ScheduleModel(models.Model):
    schedule_date = models.DateTimeField(blank=True)

    def __str__(self):
        return self.schedule_db

    class Meta:
        db_table = "schedule_db"
