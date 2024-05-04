from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Course
from .serializers import CourseSerializer
from rest_framework import permissions
from rest_framework.pagination import LimitOffsetPagination
from .filters import CourseFilter


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = LimitOffsetPagination
    filterset_class = CourseFilter