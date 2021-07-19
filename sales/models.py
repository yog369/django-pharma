from django.db import models

from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Order(models.Model):
    Order_Id = models.IntegerField()
    Transaction_id = models.PositiveBigIntegerField() 
    PJPoutlet = models.IntegerField(blank=True)
    Order_Date = models.DateField()
    Order_Time = models.TimeField()
    Order_State = models.TextField(max_length=100)
    Sku_Wise_Fulfilled_Status = models.TextField(max_length=100)
    Outlet_Id = models.IntegerField()
    Asset = models.TextField(blank=True)
    Outlet_Name = models.TextField(max_length=100)
    Type = models.TextField(max_length=100)
    Outlet_category = models.TextField(max_length=100)
    Latitude =models.FloatField() 
    Longitude = models.FloatField() 
    Location =  models.TextField(blank=True)
    Phone_No = models.CharField(max_length=12)
    Email = models.EmailField(max_length=254,blank = True)
    Owner_Name = models.TextField(max_length=100)
    Mobile_No = models.CharField(max_length=12)
    City = models.CharField(max_length=12)
    State = models.CharField(max_length=12)
    PIN = models.IntegerField(blank=True)
    Area = models.CharField(max_length=12)
    Warehouse = models.TextField(max_length=100)
    User = models.TextField(max_length=100)
    ASM  = models.TextField(max_length=100)
    Headquarter = models.CharField(max_length=20)
    Employee_Id = models.IntegerField(blank=True)
    skuid = models.IntegerField(blank=True)
    SKU_Placed = models.TextField(max_length=100)
    SKU_Code = models.CharField(max_length=12)
    HSN_Code = models.IntegerField(default=0)
    Brand = models.CharField(max_length=12)
    Category = models.CharField(max_length=12)
    Quantity_In_Units = models.IntegerField()
    Fulfilled_Sku_Quantity = models.IntegerField(default=0)
    Discount_Scheme = models.IntegerField(default=0)
    Unit_Price = models.DecimalField(max_digits=5, decimal_places=2)
    Amount = models.DecimalField(max_digits=5, decimal_places=2)
    Gross_Value = models.DecimalField(max_digits=5, decimal_places=2)
    Beat =  models.TextField(max_length=100)
    New_District_New_Taluka = models.TextField(max_length=100)
    Comment = models.TextField(blank=True)
    Workflow_Reason = models.TextField(blank=True)
    Through_Sale = models.TextField(blank=True)
    Outlet_Potential = models.TextField(blank=True)
    Focussed_Subcategory = models.TextField(blank=True)
    Competitor_Products = models.TextField(blank=True)
    flag = models.BooleanField(default=False)
    status = models.IntegerField()
    created_at = models.DateField()
    updated_at = models.DateField()
    class Meta:
      unique_together = ('Order_Id', 'skuid',)
    def __str__(self):
        return self.gd1

