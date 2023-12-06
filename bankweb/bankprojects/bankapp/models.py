from django.core.exceptions import ValidationError
from django.db import models


class Form(models.Model):
    Name = models.CharField(max_length=200,null=True,blank=True)
    DOB = models.DateField()
    Phone = models.CharField(max_length=15)
    Age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=4,null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    Address = models.TextField()
    District = models.CharField(max_length=100,null=True, blank=True)
    Branches = models.CharField(max_length=100,null=True, blank=True)
    Account_type = models.CharField(max_length=10,null=True, blank=True)
    Material = models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return self.Name
