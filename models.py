from django.db import models

# Create your models here.
class mydetails(models.Model):
    name=models.CharField(max_length=200)
    roll=models.IntegerField()
    college=models.CharField(max_length=200)
    description=models.TextField()