from .models import imageFile
from rest_framework import viewsets, permissions
from .serializers import FontSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = imageFile.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FontSerializer 