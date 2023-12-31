# Generated by Django 4.2.7 on 2023-12-07 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_rename_lesson_lessons'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('video_title', models.CharField(max_length=50)),
                ('video_upload_url', models.CharField(max_length=250, verbose_name='Video location name')),
                ('duration', models.CharField(max_length=20)),
                ('thumbnail', models.CharField(max_length=250, verbose_name='Thumbnail location name')),
                ('note', models.TextField(blank=True, null=True)),
                ('video_file', models.CharField(max_length=250, verbose_name='Video location name')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.lessons')),
            ],
        ),
    ]
