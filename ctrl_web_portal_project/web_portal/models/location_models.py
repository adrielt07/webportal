from django.db import models
from django.urls import reverse

class CountryModel(models.Model):
    id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.country_name

    class Meta:
        db_table = "country_db"


class StateModel(models.Model):
    id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=64)
    short_name = models.CharField(max_length=4)
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.state_name}, {self.short_name}"

    class Meta:
        db_table = "state_db"


class AddressModel(models.Model):
    id = models.AutoField(primary_key=True)
    street_address = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=32)
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE)
    state = models.ForeignKey(StateModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.street_address}"

    class Meta:
        db_table = "address_model"
