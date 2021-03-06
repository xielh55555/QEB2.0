# Generated by Django 3.2.7 on 2021-10-01 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_auto_20211001_1852'),
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('money', models.FloatField(max_length=50)),
                ('date', models.DateField()),
                ('year', models.IntegerField(choices=[(2020, 2020), (2021, 2021)], default=2021)),
                ('month', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], default=10)),
                ('follow', models.CharField(choices=[('王', '王雨晴'), ('胡', '胡雅丽'), ('谢', '谢立虎'), ('刘', '刘玲'), ('陈', '米如'), ('李', '李兰')], max_length=50)),
                ('attribute', models.CharField(choices=[('新', '新生'), ('老', '续费')], max_length=50)),
                ('remarks', models.CharField(max_length=200)),
            ],
        ),
    ]
