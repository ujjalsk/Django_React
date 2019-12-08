from django.db import models


class Os_name(models.Model):
    os_name = models.CharField(max_length=120)
    def __str__(self):
        return self.os_name