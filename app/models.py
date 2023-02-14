from django.db import models

# Create your models here.
class videoFile(models.Model):
    title = models.CharField(max_length=250)
    video = models.FileField(upload_to="videos/")