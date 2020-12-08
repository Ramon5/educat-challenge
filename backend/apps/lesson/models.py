from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _


class Lesson(models.Model):

    discipline = models.ForeignKey("disciplines.Discipline", on_delete=models.CASCADE)
    created_at = models.DateField(_("date"), auto_now=True)
    item_list = models.ManyToManyField("lesson.ItemList")

    class Meta:
        unique_together = ["discipline", "created_at"]

    def get_student_list(self):
        return [item for item in self.item_list.all()]

    @classmethod
    def get_attendance_list_by_date(cls, date):
        return cls.objects.filter(created_at=date)


class ItemList(models.Model):

    discipline = models.ForeignKey("disciplines.Discipline", on_delete=models.CASCADE)
    student = models.ForeignKey("students.Student", on_delete=models.CASCADE)
    status = models.BooleanField(_("status"), null=True, default=None)

    def __str__(self):
        return f"{self.student.name}"
