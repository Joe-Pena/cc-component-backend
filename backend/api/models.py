from django.db import models
from jsonfield import JSONField


class Recommendation(models.Model):
    updated_date = models.CharField(max_length=250)
    card_type = models.CharField(max_length=250)
    credit_rating = models.CharField(max_length=250)
    intro_text = models.CharField(max_length=250, blank=True)
    cta_text = models.CharField(max_length=250, blank=True)
    card1 = JSONField(null=True)
    card2 = JSONField(null=True)
    error_text = models.CharField(max_length=250)
    maintenance_text = models.CharField(max_length=250)
