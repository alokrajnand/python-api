# Generated by Django 3.0.3 on 2020-05-03 15:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_header', models.CharField(max_length=100, unique=True)),
                ('school_Name', models.CharField(max_length=100, null=True, unique=True)),
                ('school_country', models.CharField(max_length=30, null=True)),
                ('school_state', models.CharField(max_length=30, null=True)),
                ('school_city', models.CharField(max_length=30, null=True)),
                ('school_location', models.CharField(max_length=30, null=True)),
                ('school_pincode', models.IntegerField()),
                ('School_address', models.CharField(max_length=100, null=True)),
                ('School_longitude', models.CharField(max_length=100, null=True)),
                ('School_latitude', models.CharField(max_length=100, null=True)),
                ('School_map_share_link', models.CharField(max_length=200, null=True)),
                ('School_type', models.CharField(max_length=30, null=True)),
                ('School_board', models.CharField(max_length=30, null=True)),
                ('School_medium', models.CharField(max_length=30, null=True)),
                ('School_owned_by', models.CharField(max_length=30, null=True)),
                ('School_phone_number', models.IntegerField()),
                ('School_website_url', models.CharField(max_length=50, null=True)),
                ('School_mailing_address', models.CharField(max_length=50, null=True)),
                ('School_about', models.CharField(max_length=1000, null=True)),
                ('School_admission_process', models.CharField(max_length=1000, null=True)),
                ('school_start_date', models.DateField(null=True)),
                ('created_dt', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('updated_dt', models.DateTimeField(default=datetime.datetime.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_main_image_url', models.CharField(max_length=100, null=True)),
                ('school_thumbnail_image_url', models.CharField(max_length=100, null=True)),
                ('school_image_alt', models.CharField(max_length=100, null=True)),
                ('school_image_desc', models.CharField(max_length=100, null=True)),
                ('created_dt', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('updated_dt', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('school_header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.School', to_field='school_header')),
            ],
        ),
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=20, null=True)),
                ('grade_desc', models.CharField(max_length=50, null=True)),
                ('grade_fee', models.IntegerField()),
                ('created_dt', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('updated_dt', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('school_header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.School', to_field='school_header')),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_Library', models.CharField(max_length=10, null=True)),
                ('school_playground', models.CharField(max_length=10, null=True)),
                ('school_science_Lab', models.CharField(max_length=10, null=True)),
                ('school_Computer_Lab', models.CharField(max_length=10, null=True)),
                ('school_auditorium', models.CharField(max_length=10, null=True)),
                ('school_music_club', models.CharField(max_length=10, null=True)),
                ('school_drama_club', models.CharField(max_length=10, null=True)),
                ('school_Swimming_pool', models.CharField(max_length=10, null=True)),
                ('school_transport_facilities', models.CharField(max_length=10, null=True)),
                ('school_smart_classroom', models.CharField(max_length=10, null=True)),
                ('school_Number_of_teachers', models.CharField(max_length=10, null=True)),
                ('school_number_of_class_room', models.CharField(max_length=10, null=True)),
                ('school_student_per_classroom', models.CharField(max_length=10, null=True)),
                ('school_disabled_friendly', models.CharField(max_length=10, null=True)),
                ('school_hostel', models.CharField(max_length=10, null=True)),
                ('created_dt', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('updated_dt', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('school_header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.School', to_field='school_header')),
            ],
        ),
    ]
