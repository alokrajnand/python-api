# Generated by Django 3.0.3 on 2020-05-05 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_auto_20200505_0455'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='big',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='gallery',
            name='medium',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='gallery',
            name='small',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
