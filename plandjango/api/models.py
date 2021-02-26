from django.db import models

class Plan(models.Model):
 item = models.CharField(max_length=500)
