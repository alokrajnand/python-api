# Generated by Django 3.0.3 on 2020-05-05 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='School_about',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='School_phone_number',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
