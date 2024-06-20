from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Import your AnnotationViewSet class (replace with the actual name)
from .viewsets import AnnotationViewSet

router = DefaultRouter()
router.register(r'annotations', AnnotationViewSet)  # Register your viewset

urlpatterns = [
    path('', include(router.urls)),  # Include router patterns
]
