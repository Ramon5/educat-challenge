import pytest
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APIClient

from apps.lesson.models import Lesson
from tests.factories import DisciplineFactory, ItemListFactory, LessonFactory


@pytest.mark.django_db
class TestCase:
    client = APIClient()
    url = lambda id: reverse("aula", args=(id,))

    def test_should_return_attendance_list_by_date(self):
        today = timezone.now()
        discipline = DisciplineFactory.create()
        item_list = [
            ItemListFactory.create(discipline=discipline),
            ItemListFactory.create(discipline=discipline),
            ItemListFactory.create(discipline=discipline),
            ItemListFactory.create(discipline=discipline),
        ]
        lesson = LessonFactory.create(item_list=item_list)

        queryset = Lesson.get_attendance_list_by_date(today.date())

        assert queryset.count() == 1
        assert queryset[0].item_list.count() == len(item_list)

    def test_should_update_student_status_in_lesson(self):
        lesson = LessonFactory.create()
        item = ItemListFactory.create(discipline=lesson.discipline)

        assert item.status == None

        lesson.item_list.add(item)

        url = lambda discipline, item: reverse("aula", args=(discipline, item))

        response = self.client.patch(
            url(item.discipline.id, item.id), {"status": True}, format="json"
        )

        assert response.status_code == status.HTTP_200_OK
