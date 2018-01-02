from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)
    # These fields are optional
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='imgs', blank=True)

    def __unicode__(self):
        return self.user.username
        """
class Singleoption(models.Model):
    question = models.CharField(max_length=500)
    pub = models.DateTimeField('Date Published')
    choice1 = models.CharField(max_length=500,blank="True")
    choice2 = models.CharField(max_length=500, blank="True")
    choice3 = models.CharField(max_length=500, blank="True")
    choice4 = models.CharField(max_length=500, blank="True")
    answer = models.CharField(max_length=500,blank="True")
    def __str__(self):
        return self.question

class Morethanone(models.Model):
    question = models.CharField(max_length=500)
    pub = models.DateTimeField('Date Published')
    choice1 = models.CharField(max_length=500, blank="True")
    choice2 = models.CharField(max_length=500, blank="True")
    choice3 = models.CharField(max_length=500, blank="True")
    choice4 = models.CharField(max_length=500, blank="True")
    answer = models.CharField(max_length=500, blank="True")

    def __str__(self):
        return self.question

class Feedback(models.Model):

    firstname = models.CharField(max_length=1000)
    lastname = models.CharField(max_length=1000)
    email = models.EmailField(max_length=1000)
    suggestions = models.TextField(max_length=20000)
    def __str__(self):
        return self.firstname
class Login(models.Model):
    username = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)
    def __str__(self):
        return self.username
class Contact(models.Model):
    firstname = models.CharField(max_length=1000)
    lastname = models.CharField(max_length=1000)
    state = models.CharField(max_length=2000)
    subject = models.CharField(max_length=5000)
    def __str__(self):
        return self.firstname
class Blog(models.Model):
    title = models.CharField(max_length=1000)
    subject = models.CharField(max_length=100)
    username = models.CharField(max_length=1000)
    text = models.CharField(max_length=10000)
    def __str__(self):
        return self.title
class Notification(models.Model):
    category = models.CharField(max_length=100)
    notify = models.CharField(max_length=100)
    pub = models.DateTimeField('Date of notification', blank=True, null=True)
    def __str__(self):
        return self.category
class Performance(models.Model):
    user = models.CharField(max_length=100)
    datetime = models.CharField(max_length=60)
    score = models.IntegerField()
    def __str__(self):
        return self.user+' '+self.datetime


