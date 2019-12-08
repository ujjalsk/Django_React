from django.db import models

class Catagory(models.Model):
    catagory = models.CharField(max_length=120)
    class Meta:
        verbose_name_plural = 'Catagories'
    def __str__(self):
        return self.catagory

class Sub_Catagory(models.Model):
    sub_catagory = models.CharField(max_length=120)
    class Meta:
        verbose_name_plural = 'Sub_Catagories'
    def __str__(self):
        return self.sub_catagory