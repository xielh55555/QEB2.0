# Generated by Django 3.1.3 on 2021-09-20 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainqeb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Remaining_lesson_J',
            field=models.IntegerField(default=0),
        ),
    ]
