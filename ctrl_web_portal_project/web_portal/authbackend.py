from web_portal.models import AccountModel
from django.core.exceptions import ValidationError


class EmailAuthBackend(object):

    def authenticate(self, request, username=None, password=None):
        try:
            user = AccountModel.objects.get(email=username)
            if user.check_password(password):
                return user
            else:
                return None
        except AccountModel.DoesNotExist:
            raise ValidationError("Invalid credentials")

    def get_user(self, user_id):
        try:
            return AccountModel.objects.get(pk=user_id)
        except AccountModel.DoesNotExist:
            return None
