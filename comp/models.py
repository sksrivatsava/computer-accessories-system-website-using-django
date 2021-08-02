from django.db import models

# Create your models here.
class products(models.Model):
    name= models.CharField(max_length=100)
    img = models.ImageField(upload_to='images')
    desc=models.TextField()
    price=models.IntegerField()

class address(models.Model):
    name=models.CharField(max_length=100)
    product=models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    street=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.CharField(max_length=100)
    cell=models.CharField(max_length=100)

 