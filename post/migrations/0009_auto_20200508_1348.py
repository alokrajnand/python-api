# Generated by Django 3.0.3 on 2020-05-08 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_Name',
            new_name='post_name',
        ),
    ]
