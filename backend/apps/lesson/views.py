from datetime import datetime

from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response

from .queries import get_or_create_attendance_list
from .serializers import ItemList, ItemListSerializer, Lesson, LessonSerializer


class LessonView(generics.ListAPIView, generics.CreateAPIView):

    serializer_class = LessonSerializer

    def options(self, request, **kwargs):
        serialized_data = self.serializer_class.get_options(kwargs.get("discipline_id"))
        return Response(serialized_data, status=status.HTTP_200_OK)

    def get(self, request, **kwargs):
        lesson = self.get_queryset()

        serializer = self.serializer_class(lesson)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        id = self.kwargs.get("discipline_id")
        lesson = get_or_create_attendance_list(id)

        return lesson


class ItemListView(generics.UpdateAPIView):

    serializer_class = ItemListSerializer

    def post(self, request, discipline_id, id):
        item = get_object_or_404(ItemList, pk=id, discipline__pk=discipline_id)
        payload = request.data.copy()

        payload["student"] = item.student.id
        payload["discipline"] = item.discipline.id

        serializer = self.serializer_class(item, payload)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    patch = post
    put = post
