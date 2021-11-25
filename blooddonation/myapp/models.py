from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50,blank=False)
    phone = models.CharField(max_length=11,blank=False)
    email = models.EmailField(max_length=254,blank=False)
    subject = models.CharField(max_length=150,blank=False)
    message = models.TextField(blank=False)

    class Meta:
        ordering = ('name',)
    

    def __str__(self):
        return self.subject
    




class Article(models.Model):
    name = models.CharField(max_length=50)
    body = models.TextField()
    published = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now=False)

    class Meta:

        ordering = ('name',)

    def __str__(self):
        return self.name
    
class City(models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    

class Thana(models.Model):

    name = models.CharField(max_length=50)
    
    
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Bloodgroup(models.Model):

    name = models.CharField(max_length=50)
    
    
    class Meta:
        ordering = ('name',)
 

    def __str__(self):
        return self.name


class Donation(models.Model):
    name = models.CharField(max_length=50,blank=False)
    phone = models.CharField(max_length=11,blank=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE,blank=False)
    thana = models.ForeignKey(Thana, on_delete=models.CASCADE,blank=False)
    bloodgroup = models.ForeignKey(Bloodgroup, on_delete=models.CASCADE,blank=False)
    last_donation = models.DateTimeField(auto_now_add=False)

    class Meta:
        ordering = ('name',)
        

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    thana = models.ForeignKey(Thana, on_delete=models.CASCADE)
    blood = models.ForeignKey(Bloodgroup, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)
    

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'Profile for user {self.user.username}'



class RequestChange(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    body = models.TextField()

    def __str__(self):
        return self.username
    