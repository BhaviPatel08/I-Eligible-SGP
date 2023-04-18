from django.contrib import admin

# Register your models here.
from .models import School, College

admin.site.register(School)
admin.site.register(College)
