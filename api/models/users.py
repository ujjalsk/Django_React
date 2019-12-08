from django.db import models
from .items import ItemsModel
from django.contrib.auth.models import User


class UserModel(models.Model):
    # user_id = models.AutoField
    # user_name = models.CharField(max_length=120, default='')
    woner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='usermodel', null=True)
    password = models.CharField(max_length=120, default='', null=True)
    name = models.CharField(max_length=120, default='', null=True)
    email = models.EmailField(max_length=120, unique=True, null=True)
    image = models.ImageField(upload_to='images', default='', null=True)
    address = models.TextField(max_length=240, default='', null=True)
    pin = models.CharField(max_length=120, default='', null=True)
    mobile_number = models.CharField(max_length=120, default='', null=True)
    state = models.CharField(max_length=120, default='West Bengal')
    cart_item_name = models.ForeignKey(
        'ItemsModel', on_delete=models.CASCADE, null=True)
    cart_item_quantity = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.name
