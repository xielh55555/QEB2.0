# Generated by Django 3.2.7 on 2021-10-02 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainqeb', '0003_remove_student_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='imgae',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='照片'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='curriculum',
            field=models.ManyToManyField(default=' ', to='mainqeb.Curriculum', verbose_name='课程'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(default=' ', max_length=10),
        ),
    ]
