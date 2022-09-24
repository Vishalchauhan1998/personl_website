from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    photo = models.ImageField(upload_to='author/')
    about = models.TextField()
    gender_choice = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    address = models.TextField()
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    gender = models.CharField(choices=gender_choice, max_length=5)
    facebook_url = models.URLField(null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    github_url = models.URLField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    Course_Name = models.CharField(max_length=45)
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(upload_to='Course/')
    Description = models.TextField()
    Category_choice = (
        ('Machine Learning', 'machine learning'),
        ('Data Science & Ai', 'data science & ai'),
        ('Cloud Computing', 'cloud computing')
    )
    Category = models.CharField(choices=Category_choice, max_length=50)
    Project_url = models.URLField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Course_Name

class Project(models.Model):
    Project_Name = models.CharField(max_length = 100)
    User = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    Platform = models.CharField(max_length = 50)
    Technologies = models.CharField(max_length = 50)
    Description =  models.TextField()
    Category_choice = (
        ('machine learning', 'Machine Learning'),
        ('data science ', 'Data Science '),
        ('web', 'Web'),
        ('android app','Android')
    )
    Category = models.CharField(choices=Category_choice, max_length=100)
    Github_url = models.URLField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Project_Name
