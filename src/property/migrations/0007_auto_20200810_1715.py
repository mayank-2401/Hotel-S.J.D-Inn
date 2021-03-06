# Generated by Django 3.1 on 2020-08-10 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_property_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Catogery', 'verbose_name_plural': 'Catogeries'},
        ),
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name': 'Property', 'verbose_name_plural': 'Properties'},
        ),
        migrations.AlterField(
            model_name='property',
            name='type',
            field=models.CharField(choices=[('Non AC Saver (2X)', 'Non AC Saver (2X)'), ('Classic (2X)', 'Classic (2X)'), ('Delux (3X)', 'Delux (3X)')], max_length=100),
        ),
    ]
