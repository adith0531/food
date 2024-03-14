from django.db import models
from adminapp.models import *
# Create your models here.
class Statemodel(models.Model):
    State_id=models.IntegerField(primary_key=True)
    State_name=models.CharField(max_length=200)

    class Meta:
        db_table='State_table'

    def __str__(self):
        return self.State_name

class Citymodel(models.Model):
    City_id=models.IntegerField(primary_key=True)
    City_name=models.CharField(max_length=200)
    State=models.ForeignKey(Statemodel,on_delete=models.CASCADE,null=True)

    class Meta:
        db_table='City_table'

    def __str__(self):
        return self.State
class Restaurantmodel(models.Model):
    Restaurant_id=models.IntegerField(primary_key=True)
    Restaurant_name=models.CharField(max_length=200)
    Password=models.CharField(max_length=200)
    License=models.CharField(max_length=200)
    Address=models.CharField(max_length=200)
    City=models.ForeignKey(Citymodel,on_delete=models.CASCADE)
    Discription=models.TextField()
    Phone_no=models.CharField(max_length=100)
    Email=models.CharField(max_length=200)
    Image=models.ImageField()
    Host_status=models.CharField(max_length=200)

    class Meta:
        db_table='Resturent_table'

    def __str__(self):
        return self.City
class Itemmodel(models.Model):
    Item_id=models.IntegerField(primary_key=True)
    Item_name=models.CharField(max_length=200)
    Description=models.TextField()
    Price=models.FloatField()
    Quantity=models.CharField(max_length=200)
    Start_time=models.DateTimeField()
    End_time=models.DateTimeField()
    Category=models.ForeignKey(Subcategorymodel,on_delete=models.CASCADE,null=True)
    Host_id=models.ForeignKey(Restaurantmodel,on_delete=models.CASCADE,null=True)
    Status=models.CharField(max_length=200)

    class Meta:
        db_table='Item_table'

    def __str__(self):
        return self.Host_id
class Eventmodel(models.Model):
    Event_id=models.IntegerField(primary_key=True)
    Event_name=models.CharField(max_length=200)
    Descripition=models.TextField()
    Start_date=models.DateField()
    End_date=models.DateField()
    Status=models.CharField(max_length=200)

    class Meta:
        db_table='Event_table'

    def __str__(self):
        return self.Event_name

class Discountmodel(models.Model):
    Discount_id=models.IntegerField(primary_key=True)
    Item_id=models.ForeignKey(Itemmodel,on_delete=models.CASCADE,null=True)
    Discount=models.CharField(max_length=200)
    Event=models.ForeignKey(Eventmodel,on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'Discount_table'

    def __str__(self):
        return self.Event