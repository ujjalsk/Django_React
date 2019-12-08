from django.db import models

from .catagory import Catagory
from .mobile_features import *


class ItemsModel(models.Model):
    product_id = models.AutoField
    name = models.CharField(max_length=120, default='', unique=True)
    catagory = models.ForeignKey(
        'Catagory', on_delete=models.CASCADE, null=True)
    sub_catagory = models.CharField(max_length=120, default='')
    image = models.ImageField(upload_to='media/images', default='')
    price = models.CharField(max_length=120, default='')
    discount = models.CharField(max_length=120, default='')
    about = models.TextField(default='')
    quantity = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    os_name = models.ForeignKey('Os_name', on_delete=models.CASCADE, null=True)
    battery_capacity = models.ForeignKey(
        'Battery_capacity', on_delete=models.CASCADE, null=True)
    battery_type = models.ForeignKey(
        'Battery_type', on_delete=models.CASCADE, null=True)
    # discount = models.ForeignKey('Catagory', on_delete=models.CASCADE)
    # discount = models.ForeignKey('Catagory', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
