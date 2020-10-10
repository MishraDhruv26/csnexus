from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100, default="")
    email = models.EmailField(max_length=254, default="")
    rollno = models.CharField( max_length=50, default="")
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email
    
class Contact(models.Model):
    cname = models.CharField(max_length=100, default="")
    cemail = models.EmailField(max_length=254, default="")
    crollno = models.CharField( max_length=50, default="")
    msg = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.cemail