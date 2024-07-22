from users.models import *

from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import BaseUserManager

from django.utils import timezone
from django.utils.translation import gettext_lazy as _
class UserManager(BaseUserManager):
    def create_user(self, first_name, middle_name, last_name, email, phone, pan, password, role, maritial_status):
        email = self.normalize_email(email)
        user = self.model(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            email=email,
            phone=phone,
            pan=pan,
            role=role,
            maritial_status='married'
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, phone, pan, password, maritial_status):
        return self.create_user(
            first_name=first_name,
            middle_name='',
            last_name=last_name,
            email=email,
            phone=phone,
            pan=pan,
            password=password,
            role='super_admin',
            maritial_status='unmarried'
        )
