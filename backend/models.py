from django.db import models
from django.core.exceptions import ValidationError
import re

def validate_Name(value):
    if not re.match(r'^[A-Za-z $]', value):
        raise ValidationError('Name must contain only letters and spaces')
    return value

def validate_Phone_no(value):
    if not re.match(r'^\d{10}$',str(value)):
        raise ValidationError("Phone number must be 10 digits")
    return value

class Registration(models.Model):
    Name=models.CharField(max_length=255,validators=[validate_Name])
    Email=models.EmailField()
    DOB=models.DateField()
    Phone_no=models.CharField(max_length=10,validators=[validate_Phone_no])

    def __str__(self):
        return self.Name


