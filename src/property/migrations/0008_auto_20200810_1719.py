# Generated by Django 3.1 on 2020-08-10 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_auto_20200810_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='name',
            field=models.CharField(default='Room', max_length=50),
        ),
    ]