# Generated by Django 3.2.7 on 2021-10-02 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0005_alter_income_follow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='income',
            name='date',
        ),
    ]
