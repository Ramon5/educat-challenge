from django.urls import path

from apps.curriculum.views import StudentCurriculumDetailView, StudentCurriculumView
from apps.disciplines.views import DisciplineDetailView, DisciplineView
from apps.lesson.views import ItemListView, LessonView
from apps.students.views import StudentDetailView, StudentView

discipline_urls = [
    path("disciplinas/", DisciplineView.as_view(), name="disciplinas"),
    path("disciplina/<int:pk>", DisciplineDetailView.as_view(), name="disciplina"),
]

curriculum_urls = [
    path("grade_materias/", StudentCurriculumView.as_view(), name="grades"),
    path(
        "grade_materias/<int:student_id>",
        StudentCurriculumDetailView.as_view(),
        name="grade",
    ),
]

lesson_urls = [
    path("aula/<int:discipline_id>", LessonView.as_view()),
    path("aula/<int:discipline_id>/<str:date>", LessonView.as_view()),
    path("aula/<int:discipline_id>/item/<int:id>", ItemListView.as_view(), name="aula"),
]

student_urls = [
    path("alunos/", StudentView.as_view(), name="alunos"),
    path("aluno/<int:pk>", StudentDetailView.as_view(), name="aluno"),
]

urlpatterns = [] + discipline_urls + student_urls + curriculum_urls + lesson_urls
