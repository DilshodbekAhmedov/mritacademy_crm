from rest_framework.serializers import ModelSerializer
from .models import Teacher
from django.contrib.auth.models import User
# from courses.models import Course


# class ParentCourseSerializer(ModelSerializer):
#     class Meta:
#         model = Course
#         fields = '__all__'


class ParentUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TeacherSerializer(ModelSerializer):
    # user = ParentUserSerializer(source='user', read_only=True, many=True)
    # course = ParentCourseSerializer(source='course', read_only=True, many=True)

    class Meta:
        model = Teacher
        fields = '__all__'
