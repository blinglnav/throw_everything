from __future__ import unicode_literals
from django.db import models

# Create your models here.

class ThrowList(models.Model):
    what = models.CharField(max_length=256)
    added_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.what