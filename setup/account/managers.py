from django.contrib.auth.models import BaseUserManager
from django.db import models


class MyUserManager(BaseUserManager):
    def create_user(self, serial, full_name, tel, password):
        if not serial:
            raise ValueError('کاربر باید سریال داشته باشد')
        if not full_name:
            raise ValueError('کاربر باید نام داشته باشد')
        if not tel:
            raise ValueError('کاربر باید موبایل داشته باشد')
        user = self.model(serial=serial, full_name=full_name, tel=tel)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, serial, full_name, tel, password):
        user = self.create_user(serial, full_name, tel, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

# class ProfileManager(models.Manager):
#     def create_profile(self, user):
#         profile = self.model(user=user)
#         profile.save(using=self._db)
#         return profile
