from django.db import models
from django.urls import reverse
from web_portal.models.company_models import CompanyModel


class AccountModel(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.firstname} + {self.lastname} + {self.id}"

    class Meta:
        db_table = "accounts_db"
