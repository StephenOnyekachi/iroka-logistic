# Generated by Django 4.2.1 on 2023-07-19 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_items_delivered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='items',
            name='mode',
        ),
    ]