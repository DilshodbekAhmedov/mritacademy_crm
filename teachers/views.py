from rest_framework.viewsets import ModelViewSet
from .models import Teacher
from .serializers import TeacherSerializer


# Create your views here.

class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer




