from django.utils import timezone

from apps.disciplines.models import Discipline
from apps.lesson.models import ItemList, Lesson


def get_or_create_attendance_list(discipline_id):
    today = timezone.now().date()
    discipline = Discipline.objects.get(pk=discipline_id)
    
    lesson, created = Lesson.objects.get_or_create(
        discipline=discipline, created_at=today
    )
    
    if created:
        items = ItemList.objects.filter(discipline=discipline)
        lesson.item_list.set(items)

    return lesson
