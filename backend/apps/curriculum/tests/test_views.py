import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from tests.factories import DisciplineFactory, StudentFactory


@pytest.mark.django_db
class TestCaseStudentCurriculum:

    client = APIClient()
    url = reverse("grades")

    def test_should_create_a_curriculum_for_student(self):

        student = StudentFactory.create()
        discipline = DisciplineFactory.create()

        data = {
            "course": "Sistemas de Informação",
            "student": student.id,
            "discipline": discipline.id,
        }

        response = self.client.post(self.url, data=data, format="json")

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()["course"] == data["course"]

    def test_should_fail_when_try_create_curriculum_less_required_params(self):
        student = StudentFactory.create()
        discipline = DisciplineFactory.create()

        data = {
            "student": student.id,
            "discipline": discipline.id,
        }

        response = self.client.post(self.url, data=data, format="json")

        assert response.status_code == status.HTTP_400_BAD_REQUEST
