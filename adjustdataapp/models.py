from django.db import models
from django.utils.timezone import now


# Create your models here.
class DataSet(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_date = models.DateField(auto_created=True, default=now, blank=True)
    updated_date = models.DateField(auto_now=True, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    channel = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    os = models.CharField(max_length=25, null=True, blank=True)
    impressions = models.IntegerField(default=0,null=True, blank=True)
    clicks = models.IntegerField(default=0, null=True, blank=True)
    installs = models.IntegerField(default=0, null=True, blank=True)
    spend = models.DecimalField(max_digits=25, decimal_places=2, null=True, blank=True)
    revenue = models.DecimalField(max_digits=25, decimal_places=2, null=True, blank=True)
    cpi = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = 'performancematrics'
