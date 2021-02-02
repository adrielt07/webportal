from django.db import models
from django.urls import reverse

class CompanyModel(models.Model):
    company_name = models.CharField(max_length=64)    

    def __str__(self):
        return self.company_name

    class Meta:
        db_table = "company_db"
