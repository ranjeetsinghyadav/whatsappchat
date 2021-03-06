from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
