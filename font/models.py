from django.db import models

# Create your models here.
class fontFile(models.Model):
    title = models.CharField(max_length=250)
    font = models.FileField(upload_to="fonts/")