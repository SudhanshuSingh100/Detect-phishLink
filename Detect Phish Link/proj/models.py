from django.db import models

class Task(models.Model):
    url = models.TextField(null=False)
    processed = models.BooleanField(default=False)
    result = models.TextField()
