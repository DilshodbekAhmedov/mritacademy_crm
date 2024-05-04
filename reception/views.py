from rest_framework import viewsets
from.models import EnrollCourse
from .serializers import EnrollCourseSerializer


class EnrollCourseViewSet(viewsets.ModelViewSet):
    queryset = EnrollCourse.objects.all()
    serializer_class = EnrollCourseSerializer