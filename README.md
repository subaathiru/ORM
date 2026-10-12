# Ex02 Django ORM Web Application
## Date: 06.10.26

## AIM
To develop a Django Application to store and retrieve data from a Vehicle Service Database platform using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import vehicleservice_DB,vehicleservice_DBAdmin
admin.site.register(vehicleservice_DB,vehicleservice_DBAdmin)

models.py

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
```

## OUTPUT
![alt text](<Screenshot 2026-10-12 132522.png>)


## RESULT
Thus the program for creating Online Food Delivery Database using ORM hass been executed successfully
