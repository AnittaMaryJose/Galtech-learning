# Generated by Django 4.2.7 on 2023-12-06 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_courses_id_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
