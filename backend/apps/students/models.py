from django.db import models
from django.utils.translation import gettext as _


class Student(models.Model):

    name = models.CharField(_("name"), max_length=150)

    class Meta:
        ordering = ["name"]
        indexes = [models.Index(fields=["name",])]

    def __str__(self):
        return self.name
