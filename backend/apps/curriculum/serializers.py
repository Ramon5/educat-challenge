from rest_framework import serializers

from apps.disciplines.serializers import DisciplineSerializer
from apps.students.serializers import StudentSerializer

from .models import StudentCurriculum


class StudentCurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCurriculum
        fields = "__all__"
