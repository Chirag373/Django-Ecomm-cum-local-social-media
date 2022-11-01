
from django.contrib import admin
from . import models
# Register your models here.

class Postadmin(admin.ModelAdmin):
    fields = ["category", "title", "price", "img", "description"]


admin.site.register(models.UserMaster)
admin.site.register(models.Registeruser)
admin.site.register(models.Postuser, Postadmin)
admin.site.register(models.Query)
