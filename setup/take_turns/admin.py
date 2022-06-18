from django.contrib import admin
from . import models

admin.site.register(models.Doctor)
admin.site.register(models.Presence)
admin.site.register(models.Visit)
# Register your models here.
