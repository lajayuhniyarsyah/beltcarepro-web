from django.contrib import admin

# Register your models here.
from .models import Customer,Site

class CustomerAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'co_type', 'active') 
admin.site.register(Customer)
admin.site.register(Site)