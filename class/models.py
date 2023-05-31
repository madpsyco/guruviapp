
from django.core.validators import FileExtensionValidator
from django.db import models



class Classes(models.Model):
    videoname = models.CharField(max_length=250)
    videonumber = models.CharField(max_length=15)
    duration = models.CharField(max_length=25)
    section = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos_uploaded/',validators=[FileExtensionValidator(allowed_extensions=['MOV','avi', 'mp4', 'webm', 'mkv'])])
    date_uploaded = models.DateTimeField()

    def __str__(self):
        return self.videoname