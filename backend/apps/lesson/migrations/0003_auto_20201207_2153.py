# Generated by Django 3.1.4 on 2020-12-08 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disciplines', '0002_auto_20201207_2038'),
        ('lesson', '0002_auto_20201206_2221'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='lesson',
            unique_together=set(),
        ),
        migrations.AlterIndexTogether(
            name='lesson',
            index_together={('discipline', 'created_at')},
        ),
    ]