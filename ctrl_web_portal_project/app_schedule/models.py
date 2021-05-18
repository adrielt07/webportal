from django.db import models
from web_portal.models.company_models import CompanyModel
from web_portal.models import AccountModel

# Create your models here.
class ScheduleModel(models.Model):
    schedule_date = models.DateTimeField(blank=True)
    canceled = models.BooleanField(default=False)
    company = models.ForeignKey(
        CompanyModel,
        on_delete=models.CASCADE,
        related_name='schedule',
        null=True,
    )
    user = models.ForeignKey(
        AccountModel,
        on_delete=models.CASCADE,
        null=True)

    def __str__(self):
        return f"{self.company} - {self.id}"

    class Meta:
        db_table = "schedule_db"
