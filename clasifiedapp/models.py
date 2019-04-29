from django.db import models


# Create your models here.


class Users(models.Model):
    firstname = models.CharField(max_length=215,null=True,blank=True)
    lastname = models.CharField(max_length=512,null=True,blank=True)
    username = models.CharField(max_length=215,null=True,blank=True)
    email = models.EmailField(max_length=215,unique=True,null=False,blank=False)
    password = models.CharField(max_length=512,null=True,blank=True)
    photo = models.ImageField(upload_to='Photos/', null=True, blank=True)
    modefied_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.name