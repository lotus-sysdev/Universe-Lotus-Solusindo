# Generated by Django 4.2.10 on 2024-03-08 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page1', '0010_alter_events_package_mass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='SKU',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]
