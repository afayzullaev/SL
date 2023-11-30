from django.db import models

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=400)
    location = models.TextField(blank=True)
    imei = models.CharField(max_length=16, blank=False,null=False,unique=True)
    state = models.BooleanField(default=False)
    is_on_time = models.TimeField()
    is_off_time = models.TimeField()