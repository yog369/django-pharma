from django.contrib import admin

# Register your models here.
from .models import Order
from import_export import resources
from import_export.admin import ImportExportModelAdmin


@admin.register(Order)
class OrderResource(ImportExportModelAdmin):
    list_display=('Order_Id','skuid','created_at',)
    pass

class OrderAdmin(admin.ModelAdmin):
    list_display=('Order_Id','Outlet_Name','skuid','created_at',)
    search_fields=('Order_Id','Outlet_Name','skuid','created_at',)


#admin.site.register(Order,OrderAdmin)