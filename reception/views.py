from rest_framework import viewsets
from.models import EnrollCourse
from.serializers import ReceptionSerializer

class EnrollCourseViewSet(viewsets.ModelViewSet):
    queryset = EnrollCourse.objects.all()
    serializer_class = ReceptionSerializer
