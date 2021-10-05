# Generated by Django 3.2.7 on 2021-10-01 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='expenditure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('money', models.FloatField(max_length=50)),
                ('date', models.DateField()),
                ('remarks', models.CharField(max_length=200)),
            ],
        ),
    ]
