from django.db import models
from datetime import datetime

# Create your models here.


class mydata(models.Model):
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=100)
    created_at=models.DateTimeField(default=datetime.now(),blank=True)
    updated_at=models.DateTimeField(default=datetime.now(),blank=True)
    