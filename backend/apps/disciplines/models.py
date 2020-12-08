from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _

from apps.lesson.models import Lesson


class Discipline(models.Model):

    name = models.CharField(_("name"), max_length=50)

    class Meta:
        ordering = ["name"]
        indexes = [models.Index(fields=["name",])]

    def __str__(self):
        return self.name

    def get_attendance_list_by_date(cls, date):
        return Lesson.objects.filter(discipline=self, created_at=date)

    @classmethod
    def get_attendance_list_by_discipline(cls, discipline, date=None):
        queryset = Lesson.objects.filter(discipline=discipline)
        if date:
            return queryset.filter(created_at=date)
        return queryset
