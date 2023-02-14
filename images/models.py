from django.db import models

# Create your models here.
class imageFile(models.Model):
    title = models.CharField(max_length=250)
    image = models.FileField(upload_to="images/")