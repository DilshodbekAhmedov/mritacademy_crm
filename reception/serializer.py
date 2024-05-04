from rest_framework import serializers
from.models import EnrollCourse

class ReceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnrollCourse
        fields = ['id', 'name', 'surname', 'number', 'course', 'time', 'w_time', 'created']
        read_only_fields = ['id', 'created']