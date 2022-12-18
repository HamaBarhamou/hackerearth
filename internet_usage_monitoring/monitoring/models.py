from django.db import models


# Create your models here.
class Monitoring(models.Model):
    username = models.CharField(max_length=100)
    mac_adresse = models.CharField(max_length=100)
    start_time = models.DateTimeField(default=None)
    usage_time = models.TimeField(default=None)
    upload = models.DecimalField(
                blank=True,
                null=True,
                max_digits=20,
                decimal_places=10
                )
    download = models.DecimalField(
                blank=True,
                null=True,
                max_digits=20,
                decimal_places=10
                )
