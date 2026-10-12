from  django.db import models
from  django.contrib import admin
class vehicleservice_DB(models.Model):
    Vehicle_Type=models.CharField(max_length=10)
    Vehicle_No=models.CharField(max_length=10)
    Vehicle_Name=models.CharField(max_length=10)
    Customer_Name=models.CharField(max_length=10)
    Contact_No=models.IntegerField()
    Wash_Type=models.CharField(max_length=10)
    Wash_Date=models.DateField(max_length=10)
    Payment_Status=models.CharField(max_length=10)
class vehicleservice_DBAdmin(admin.ModelAdmin):
    list_display=["Vehicle_Type","Vehicle_No","Customer_Name","Contact_No","Wash_Date","Payment_Status"]
