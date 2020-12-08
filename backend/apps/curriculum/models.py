from django.db import models
from django.utils.translation import gettext as _

from apps.lesson.models import ItemList


class StudentCurriculum(models.Model):

    course = models.CharField(_("course name"), max_length=90)
    discipline = models.ForeignKey("disciplines.Discipline", on_delete=models.CASCADE)
    student = models.ForeignKey("students.Student", on_delete=models.CASCADE)

    class Meta:
        ordering = ["-id"]
        unique_together = ["discipline", "student"]

    def __str__(self):
        return f"{self.student.name}"

    @classmethod
    def get_curriculum_by_student(cls, student):
        return cls.objects.filter(student=student)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        item, created = ItemList.objects.get_or_create(
            student=self.student, discipline=self.discipline
        )
