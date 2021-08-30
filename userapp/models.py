from django.db import models
from adminapp.models import *
# Create your models here.
class login(models.Model):

    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    role=models.CharField(max_length=100)

class register(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    log=models.ForeignKey(login,on_delete=models.CASCADE)
class details1(models.Model):
    img = models.FileField(upload_to='orders')
    user=models.CharField(max_length=100)

    proname=models.CharField(max_length=100)
    quantity=models.IntegerField()
    price=models.IntegerField()
    total=models.IntegerField()
    uid = models.ForeignKey(register, on_delete=models.CASCADE)
    pid = models.ForeignKey(products, on_delete=models.CASCADE)






