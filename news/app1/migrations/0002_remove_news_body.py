# Generated by Django 5.0.3 on 2024-04-18 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='body',
        ),
    ]
