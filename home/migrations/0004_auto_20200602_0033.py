# Generated by Django 3.0.6 on 2020-06-01 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200601_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkinclass',
            name='classname',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Tên lớp'),
        ),
        migrations.AlterField(
            model_name='checkinclass',
            name='room',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Tên phòng'),
        ),
        migrations.AlterField(
            model_name='checkinclass',
            name='student',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Tên học viên'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='classname',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Tên lớp'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='room',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Tên phòng'),
        ),
    ]
