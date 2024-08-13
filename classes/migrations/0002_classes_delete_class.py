# Generated by Django 5.0.6 on 2024-07-14 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=20)),
                ('class_id', models.PositiveSmallIntegerField()),
                ('class_course', models.CharField(max_length=20)),
                ('class_trainer', models.CharField(max_length=20)),
                ('class_daflex items-centers', models.PositiveSmallIntegerField()),
                ('academic_year', models.CharField(max_length=20)),
                ('class_capacity', models.PositiveSmallIntegerField()),
                ('class_enrollment', models.PositiveBigIntegerField()),
                ('room_number', models.PositiveSmallIntegerField()),
                ('class_windows', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Class',
        ),
    ]
