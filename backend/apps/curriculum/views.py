from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response

from .models import StudentCurriculum
from .serializers import StudentCurriculumSerializer


class StudentCurriculumView(generics.ListAPIView):

    serializer_class = StudentCurriculumSerializer

    def get(self, request):

        serializer = self.serializer_class(self.get_queryset(), many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        payload = request.data

        serializer = self.serializer_class(data=payload)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        return StudentCurriculum.objects.select_related("student", "discipline").all()


class StudentCurriculumDetailView(generics.UpdateAPIView, generics.DestroyAPIView):

    serializer_class = StudentCurriculumSerializer

    def get(self, request, student_id):

        curriculum = get_object_or_404(StudentCurriculum, student__id=student_id)

        serialized_instance = self.serializer_class(curriculum)

        return Response(serialized_instance.data, status=status.HTTP_200_OK)
