# Generated by Django 5.1.1 on 2024-09-28 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdviceApp', '0002_advice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advice',
            name='apiId',
        ),
    ]
