from django.db import models
from django.utils import timezone #module to modify date
#from django.contrib.auth.models import User #this creates an one to many relationship between user/author and post
from django.urls import reverse #alternate to redirect after creating a post
from PIL import Image #import image from pillow libarary
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


class Home(models.Model):#post class is a table in the db
    img_count = models.CharField(max_length=100, default='none')
    home_img = models.ImageField(default='default.png', blank=True, upload_to='home_img')

    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    #one to many rel between admin.user table and post(with common attribute author) using foreign key. on_delete=models.CASCADE means if the user is deleted then the post will also be deleted but if post is deleted user will remain

    def __str__(self):
        return self.img_count

class OnGoingProject(models.Model):#post class is a table in the db
    project_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    unit_size = models.CharField(max_length=100)
    expected_completion = models.DateField()
    ogp_img = models.ImageField(default='default.png', blank=True, upload_to='ongoing_project_img')
    date_posted = models.DateField(default=timezone.now)
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    #one to many rel between admin.user table and post(with common attribute author) using foreign key. on_delete=models.CASCADE means if the user is deleted then the post will also be deleted but if post is deleted user will remain

    def __str__(self):
        return self.project_name

class UpcomingProject(models.Model):#post class is a table in the db
    project_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    unit_size = models.CharField(max_length=100)
    #expected_completion = models.DateField()
    ucp_img = models.ImageField(default='http://placehold.it/700x400', blank=True, upload_to='upcoming_project_img')
    date_posted = models.DateField(default=timezone.now)
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    #one to many rel between admin.user table and post(with common attribute author) using foreign key. on_delete=models.CASCADE means if the user is deleted then the post will also be deleted but if post is deleted user will remain

    def __str__(self):
        return self.project_name


class CompletedProject(models.Model):#post class is a table in the db
    project_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    unit_size = models.CharField(max_length=100)
    completion_date = models.DateField()
    cp_img = models.ImageField(default='default.png', blank=True, upload_to='completed_project_img')
    date_posted = models.DateField(default=timezone.now)
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    #one to many rel between admin.user table and post(with common attribute author) using foreign key. on_delete=models.CASCADE means if the user is deleted then the post will also be deleted but if post is deleted user will remain

    def __str__(self):
        return self.project_name
