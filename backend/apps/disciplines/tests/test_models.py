import pytest

from tests.factories import DisciplineFactory


@pytest.mark.django_db
class TestCaseDiscipline:
    def test_return_name_on_str_model_method(self):
        discipline = DisciplineFactory.create()
        assert discipline.name == discipline.__str__()
