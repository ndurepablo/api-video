from rest_framework import serializers
from .models import imageFile

class FontSerializer(serializers.ModelSerializer):
     class Meta:
         model = imageFile
         fields = ('id', 'title', 'image')
