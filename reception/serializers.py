from rest_framework import serializers
from.models import EnrollCourse


class EnrollCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnrollCourse
        fields = ['id', 'name', 'surname', 'number', 'course', 'time', 'days', 'created']
        read_only_fields = ['id', 'created']