from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Adminmodel(models.Model):
    Admin_id=models.IntegerField(primary_key=True)
    Username=models.CharField(max_length=200)
    Password=models.CharField(max_length=200)
    Email=models.CharField(max_length=200)
    Phonenumber=models.CharField(max_length=100)

    class Meta:
        db_table='Admin_table'

    def __str__(self):
        return self.Username

class Maincategorymodel(models.Model):
    Maincategory_id=models.IntegerField(primary_key=True)
    Maincategory=models.CharField(max_length=200)
    Image=models.ImageField(upload_to='maincategory/',null=True)

    class Meta:
        db_table='Maincategory_table'

    def __str__(self):
        return self.Maincategory

class Subcategorymodel(models.Model):
    Subcategory_id=models.IntegerField(primary_key=True)
    Subcategory=models.CharField(max_length=200)
    Maincategory=models.ForeignKey(Maincategorymodel,on_delete=models.CASCADE,null=True)
    Image = models.ImageField(upload_to='Subcategory/', null=True)
    Resturant_name=models.CharField(max_length=100,null=True)
    Price=models.FloatField(null=True)
    Rating=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],null=True)



    class Meta:
        db_table='Subcategory_table'

    def __str__(self):
        return self. Subcategory