# Generated by Django 5.1.1 on 2024-09-29 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdviceApp', '0006_advice_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advice',
            name='added',
        ),
    ]
