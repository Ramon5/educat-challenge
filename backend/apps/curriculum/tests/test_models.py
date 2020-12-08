import pytest

from apps.lesson.models import ItemList
from tests.factories import StudentCurriculumFactory


@pytest.mark.django_db
class TestCaseStudentCurriculum:
    def test_return_name_on_str_model_method(self):
        curriculum = StudentCurriculumFactory.create()

        assert curriculum.student.name == curriculum.__str__()

    def test_check_create_lesson_item_list_when_create_student_curriculum(self):
        StudentCurriculumFactory.create()
        assert ItemList.objects.count() == 1

    def test_check_create_lesson_item_list_from_student(self):
        curriculum = StudentCurriculumFactory.create()
        item = ItemList.objects.latest("id")

        assert curriculum.student == item.student
        assert curriculum.discipline == item.discipline
