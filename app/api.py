from .models import videoFile
from rest_framework import viewsets, permissions
from .serializers import VideoSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = videoFile.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = VideoSerializer 