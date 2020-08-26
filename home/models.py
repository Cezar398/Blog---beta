from django.db import models

class Index(models.Model):
    nav_title = models.CharField(max_length=40, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
