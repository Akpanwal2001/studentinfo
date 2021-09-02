from django.db import models
from django.db.models.fields import CharField, IntegerField, SlugField

# Create your models here.
class Student(models.Model):
    sno = models.AutoField(primary_key=True)
    slug = SlugField(auto_created=True)
    sname = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    dob = models.DateField()
    phone = models.IntegerField(default=0)
    Class = models.IntegerField(default=0)
    percentage = models.FloatField(default=0.0)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    pincode = models.IntegerField(default=0)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sname+"'s information"
    