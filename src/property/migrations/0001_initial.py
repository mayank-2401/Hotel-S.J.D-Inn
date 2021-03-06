# Generated by Django 3.1 on 2020-08-09 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('NAS', 'Non AC Saver (2X)'), ('CLA', 'Classic (2X)'), ('DEL', 'Delux (3X)')], max_length=100)),
                ('price', models.PositiveIntegerField()),
                ('area', models.DecimalField(decimal_places=2, max_digits=8)),
                ('room_no', models.PositiveIntegerField()),
            ],
        ),
    ]
