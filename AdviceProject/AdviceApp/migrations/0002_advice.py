# Generated by Django 5.1.1 on 2024-09-26 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdviceApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apiId', models.CharField(max_length=3)),
                ('advice', models.CharField(max_length=1000)),
            ],
        ),
    ]
