from rest_framework import routers
from django.urls import path, include
from rest_framework import routers
from . import views
from .api import ImageViewSet 

router = routers.DefaultRouter()


# Wire up our API using automatic URL routing.
router.register('api/images', ImageViewSet, 'images')

urlpatterns = router.urls