# Generated by Django 3.2.7 on 2021-10-01 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_income'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='attribute',
            field=models.CharField(choices=[('新生', '新生'), ('续费', '续费')], max_length=50),
        ),
        migrations.AlterField(
            model_name='income',
            name='follow',
            field=models.CharField(choices=[('王雨晴', '王雨晴'), ('胡雅丽', '胡雅丽'), ('谢立虎', '谢立虎'), ('刘刘玲', '刘玲'), ('陈米如', '米如'), ('李兰', '李兰')], max_length=50),
        ),
    ]
