import pytest

from apps.students.models import Student
from tests.factories import StudentFactory


@pytest.mark.django_db
class TestCaseStudentCurriculum:
    def test_return_name_on_str_model_method(self):
        student = StudentFactory.create()

        assert student.name == student.__str__()

    def test_check_create_successfully_student(self):
        StudentFactory.create()
        assert Student.objects.count() == 1
