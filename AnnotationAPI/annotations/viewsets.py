
from rest_framework import viewsets
from .models import Annotation
from .serializers import AnnotationSerializer

class AnnotationViewSet(viewsets.ModelViewSet):
  queryset = Annotation.objects.all()
  serializer_class = AnnotationSerializer