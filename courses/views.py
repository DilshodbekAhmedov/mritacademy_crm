from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Course
from .serializers import CourseSerializer
from .filters import CourseFilter


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filterset_class = CourseFilter