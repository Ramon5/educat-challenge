import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from tests.factories import DisciplineFactory


@pytest.mark.django_db
class TestCaseDisciplines:

    client = APIClient()
    url = reverse("disciplinas")

    def test_should_create_successfully_discipline(self):
        data = {"name": "Analise de Algorimtos e Estrutura de Dados"}

        response = self.client.post(self.url, data, format="json")

        assert response.status_code == status.HTTP_201_CREATED
        assert data["name"] == response.json()["name"]

    def test_should_retrieve_list_disciplines(self):
        DisciplineFactory.create()
        DisciplineFactory.create()
        DisciplineFactory.create()

        response = self.client.get(self.url, format="json")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 3

    def test_should_delete_a_discipline(self):
        discipline = DisciplineFactory.create()

        url = lambda id: reverse("disciplina", args=(id,))

        response = self.client.delete(url(discipline.id))

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert response.data == {}

    def tet_should_update_discipline_information(self):

        discipline = DisciplineFactory.create()

        data = {"name": "Redes 1"}

        assert discipline.name != data["name"]

        url = lambda id: reverse("disciplina", args=(id,))
        response = self.client.patch(url(discipline.id), data=data, format="json")

        assert response.status_code == status.HTTP_200_OK
        assert response.json()["name"] == data["name"]
