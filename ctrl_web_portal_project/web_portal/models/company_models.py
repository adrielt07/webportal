from django.db import models
from django.urls import reverse
from web_portal.models.location_models import AddressModel
from phonenumber_field.modelfields import PhoneNumberField

class CompanyModel(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=64)
    address = models.ForeignKey(AddressModel, on_delete=models.CASCADE)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.company_name

    class Meta:
        db_table = "company_db"
