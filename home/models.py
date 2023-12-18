from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
import os
import uuid


# Create your models here.
def unique_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join('profile_pics', filename)

    
    
              
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
   
    profile_picture = models.ImageField(
        upload_to=unique_name,
        blank=True,
        null=True, 
        default='profile_pics/avatar.png'
    )
    
    create_at = models.DateField(null=True, blank=True, auto_now=True)
    update_at = models.DateField(null=True, blank=True, auto_now=True)
    delete_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
    
    

COURSE_STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

COURSE_TYPE_CHOICES = [
        (True, 'Paid'),
        (False, 'Unpaid'),
    ]

class courses(models.Model):
    course_name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='course_name', unique=True, null=True)
    course_fee = models.CharField(max_length=255)
    course_description = models.TextField()
    course_type = models.BooleanField(choices=COURSE_TYPE_CHOICES, default=False)
    course_status = models.CharField(max_length=10, choices=COURSE_STATUS_CHOICES, default='inactive')
    create_at = models.DateField(auto_now_add=True)
    
    image= models.ImageField(
        upload_to=unique_name,
        blank=True,
        null=True, 
       default='profile_pics/avt.jpg'
    )

    def __str__(self):
        return self.course_name

class Lessons(models.Model):
    lesson_title = models.CharField(max_length=50)
    course = models.ForeignKey('Courses', on_delete=models.CASCADE)
    lesson_order = models.IntegerField()

    def __str__(self):
        return self.lesson_title
    
class Video(models.Model):
    # id = models.IntegerField(primary_key=True)
    video_title = models.CharField(max_length=50)
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE)
    video_upload_url = models.CharField(max_length=250, help_text='Video location name')
    duration = models.CharField(max_length=20)
    thumbnail = models.CharField(max_length=250, help_text='Thumbnail location name')
    note = models.TextField(blank=True, null=True)
    video_file = models.CharField(max_length=250, help_text='Video location name')

    def __str__(self):
        return self.video_title



class Reviews(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(courses, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField()
    review_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s review for {self.course}"