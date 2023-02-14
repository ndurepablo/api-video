from .models import fontFile
from rest_framework import viewsets, permissions
from .serializers import FontSerializer

class FontViewSet(viewsets.ModelViewSet):
    queryset = fontFile.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FontSerializer 