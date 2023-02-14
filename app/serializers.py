from rest_framework import serializers
from .models import videoFile

class VideoSerializer(serializers.ModelSerializer):
     class Meta:
         model = videoFile
         fields = ('id', 'title', 'video')
