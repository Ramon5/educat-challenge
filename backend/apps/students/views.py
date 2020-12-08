from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializer


class StudentView(generics.ListAPIView, generics.CreateAPIView):

    serializer_class = StudentSerializer

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
        return Student.objects.all()


class StudentDetailView(generics.UpdateAPIView, generics.DestroyAPIView):

    serializer_class = StudentSerializer

    def get(self, request, pk):

        student = get_object_or_404(Student, pk=pk)

        serializer = self.serializer_class(student)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):

        payload = request.data

        student = get_object_or_404(Student, pk=pk)

        serializer = self.serializer_class(student, payload)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):

        student = get_object_or_404(Student, pk=pk)

        student.delete()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    patch = post
    put = post
