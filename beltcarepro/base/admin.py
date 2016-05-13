from django.contrib import admin

# Register your models here.
from .models import Customer,Site,CustomerAdmin

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Site)