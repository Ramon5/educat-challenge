import factory
from factory.django import DjangoModelFactory
from apps.students.models import Student
from apps.disciplines.models import Discipline
from apps.curriculum.models import StudentCurriculum
from apps.lesson.models import Lesson, ItemList

class StudentFactory(DjangoModelFactory):
    
    name = factory.Faker("name")

    class Meta:
        model = Student

class DisciplineFactory(DjangoModelFactory):

    name = factory.Faker("name")

    class Meta:
        model = Discipline

class StudentCurriculumFactory(DjangoModelFactory):
    
    discipline = factory.SubFactory(DisciplineFactory)
    student = factory.SubFactory(StudentFactory)

    class Meta:
        model = StudentCurriculum

class ItemListFactory(DjangoModelFactory):

    student = factory.SubFactory(StudentFactory)
    discipline = factory.SubFactory(DisciplineFactory)
    status = None

    class Meta:
        model = ItemList

class LessonFactory(DjangoModelFactory):

    discipline = factory.SubFactory(DisciplineFactory)

    class Meta:
        model = Lesson

    @factory.post_generation
    def item_list(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for item in extracted:
                self.item_list.add(item)