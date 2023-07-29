from django.db import models
from datetime import datetime,date
# Create your models here.
class Video(models.Model):
    caption=models.CharField(max_length=50)
    status=models.CharField(max_length=50,default="unverify")
    location=models.CharField(max_length=50)
    time=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    coordinates=models.CharField(max_length=50)
    description=models.CharField(max_length=50,default="NULL")
    video=models.FileField(upload_to="video/%y")
    def __str__(self):
        return self.caption
class vid(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')