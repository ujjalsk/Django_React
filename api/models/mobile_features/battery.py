from django.db import models


class Battery_type(models.Model):
    Battery_type = models.CharField(max_length=120)
    Fixed = models.BooleanField(default=False)
    def __str__(self):
        if self.Fixed == True:
            Btype = 'Fixed '+ self.Battery_type
        Btype = 'Removeable ' + self.Battery_type
        return Btype
 
class Battery_capacity(models.Model):
    Battery_capacity = models.CharField(max_length=120)
    def __str__(self):
        return self.Battery_capacity