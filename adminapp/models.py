from django.db import models
from userapp.models import *


# Create your models here.


class products(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    img=models.FileField(upload_to='products')
#class orders(models.Model):
    #product=models.CharField(max_length=100)
    #user=models.CharField(max_length=100)
    #quantity=models.IntegerField()
    #pri=models.FloatField()
    #uid=models.ForeignKey(register,on_delete=models.CASCADE)
    #pid=models.ForeignKey(products,on_delete=models.CASCADE)

#class address(models.Model):
    #name=models.CharField(max_length=100)
    #address=models.CharField(max_length=100)
