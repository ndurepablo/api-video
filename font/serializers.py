from rest_framework import serializers
from .models import fontFile

class FontSerializer(serializers.ModelSerializer):
     class Meta:
         model = fontFile
         fields = ('id', 'title', 'font')
