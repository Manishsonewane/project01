from django.db import models

# Create your models here.
from django.db import models
from django.db.models.fields import EmailField
class company(models.Model):
     Name=models.CharField(max_length=20)
     phone=models.IntegerField()
     
     email=models.EmailField(max_length=20)
     message=models.CharField(max_length=500)
     


def __str__(self):
        return self.Name 
