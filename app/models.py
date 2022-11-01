from distutils.command.upload import upload
from email.policy import default
from turtle import title
from unicodedata import category, name
from django.db import models

# Create your models here.
class UserMaster(models.Model):
    Email = models.EmailField()
    Mobile = models.CharField(max_length=50)
    Otp = models.IntegerField()
    Password = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now_add=True)

class Registeruser(models.Model):
    user_id = models.ForeignKey(UserMaster, on_delete=models.CASCADE)
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)

    def __str__(self):
        return self.Firstname

class Postuser(models.Model):
    user_id = models.ForeignKey(Registeruser, on_delete=models.CASCADE)  # type: ignore
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.IntegerField()
    img = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.title

class Query(models.Model):
    user_id = models.ForeignKey(Registeruser, on_delete=models.CASCADE)
    query = models.CharField(max_length=150)
    q_title = models.CharField(max_length=150)
    
    def __str__(self):
        return self.q_title









    
