from django.contrib import admin
from web_portal.models.account_models import AccountModel

# Register your models here.
class AccountModelAdmin(admin.ModelAdmin):
    list_display = ("id", "firstname", "lastname")

admin.site.register(AccountModel, AccountModelAdmin)
