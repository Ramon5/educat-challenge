from rest_framework import serializers

from apps.disciplines.serializers import DisciplineSerializer

from .models import ItemList, Lesson


class LessonSerializer(serializers.ModelSerializer):

    student_list = serializers.SerializerMethodField()
    discipline = DisciplineSerializer()

    class Meta:
        model = Lesson
        fields = ["id", "created_at", "discipline", "student_list"]

    def get_student_list(self, obj):
        items = obj.get_student_list()
        return [
            {"id": item.id, "name": item.student.name, "status": item.status}
            for item in items
        ]

    @classmethod
    def get_options(cls, discipline_id):

        items = ItemList.objects.filter(discipline__pk=discipline_id)

        return [
            {"id": item.id, "student": item.student.name, "status": item.status}
            for item in items
        ]


class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemList
        fields = "__all__"
