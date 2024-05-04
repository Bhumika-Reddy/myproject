from django.db import models
class Cafestore(models.Model):
    item=models.CharField(max_length=100)
    cost=models.IntegerField()
    quantity=models.IntegerField()
    time=models.IntegerField()
    

# Create your models here.
