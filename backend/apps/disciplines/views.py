from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Discipline
from .serializers import DisciplineSerializer


class DisciplineView(generics.ListAPIView, generics.CreateAPIView):

    serializer_class = DisciplineSerializer

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
        return Discipline.objects.all()


class DisciplineDetailView(generics.UpdateAPIView, generics.DestroyAPIView):

    serializer_class = DisciplineSerializer

    def get(self, request, pk):

        discipline = get_object_or_404(Discipline, pk=pk)

        serializer = self.serializer_class(discipline)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):

        discipline = get_object_or_404(Discipline, pk=pk)

        discipline.delete()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def post(self, request, pk):
        payload = request.data

        discipline = get_object_or_404(Discipline, pk=pk)

        serializer = self.serializer_class(discipline, data=payload)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    patch = post
    put = post

    def get_queryset(self):
        return Discipline.objects.all()
