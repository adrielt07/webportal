from django.db import models
from django.urls import reverse

class AccountModel(models.Model):
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    user_id = "1234"

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = "Accounts_db"
