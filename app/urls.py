from rest_framework import routers
from django.urls import path, include
from rest_framework import routers
from . import views
from .api import VideoViewSet 

router = routers.DefaultRouter()


# Wire up our API using automatic URL routing.
router.register('api/videos', VideoViewSet, 'videos')

urlpatterns = router.urls