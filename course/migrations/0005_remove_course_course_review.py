# Generated by Django 3.0.3 on 2020-04-30 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20200430_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course_review',
        ),
    ]