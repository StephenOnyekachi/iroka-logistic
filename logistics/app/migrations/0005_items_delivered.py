# Generated by Django 4.2.1 on 2023-07-19 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='delivered',
            field=models.BooleanField(default=False),
        ),
    ]
