import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from tests.factories import StudentFactory


@pytest.mark.django_db
class TestCaseStudent:
    client = APIClient()
    url = reverse("alunos")

    def test_create_student_successfully(self):
        data = {
            "name": "Fulano Teste",
        }

        response = self.client.post(self.url, data=data, format="json")

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()["name"] == data["name"]

    def test_should_fail_when_try_create_student_less_data(self):

        response = self.client.post(self.url, format="json")

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_should_return_a_students_created(self):

        students = [
            StudentFactory.create(),
            StudentFactory.create(),
            StudentFactory.create(),
        ]

        response = self.client.get(self.url, format="json")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == len(students)

    def test_should_delete_a_student(self):
        student = StudentFactory.create()

        url = lambda id: reverse("aluno", args=(id,))

        response = self.client.delete(url(student.id))

        assert response.status_code == status.HTTP_204_NO_CONTENT
