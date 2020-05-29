# Generated by Django 3.0.6 on 2020-05-27 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200527_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='adress',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Địa chỉ'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='student',
            name='identity_card',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='CMND'),
        ),
        migrations.AlterField(
            model_name='student',
            name='note',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Ghi chú'),
        ),
        migrations.AlterField(
            model_name='student',
            name='phonenumber',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='SDT'),
        ),
        migrations.AlterField(
            model_name='student',
            name='phonenumber_family',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='SDT phụ huynh'),
        ),
    ]