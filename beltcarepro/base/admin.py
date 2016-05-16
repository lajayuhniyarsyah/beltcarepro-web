from django.contrib import admin

# Register your models here.
from .models import Customer,CustomerAdmin,Site,SiteAdmin,Area,AreaAdmin,Conveyor,ConveyorAdmin

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Site,SiteAdmin)
admin.site.register(Area,AreaAdmin)
admin.site.register(Conveyor,ConveyorAdmin)