# Generated by Django 3.0.3 on 2020-04-02 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0003_profile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='profile',
            new_name='UserProfile',
        ),
    ]
