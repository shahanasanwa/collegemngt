from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    USERTYPE=models.CharField(max_length=100)

class Department(models.Model):
    DEPNAME=models.CharField(max_length=100)

class Teacher(models.Model):
    DEPID=models.ForeignKey(Department,on_delete=models.CASCADE)
    TID=models.ForeignKey(User,on_delete=models.CASCADE)
    AGE=models.IntegerField()
    ADDRESS=models.CharField(max_length=50)
    QUALIFICATION=models.CharField(max_length=100)


class Student(models.Model):
    DEPID=models.ForeignKey(Department,on_delete=models.CASCADE)
    SID=models.ForeignKey(User,on_delete=models.CASCADE)
    AGE=models.IntegerField()
    ADDRESS=models.CharField(max_length=50)





