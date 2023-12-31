# Generated by Django 4.2.7 on 2023-12-06 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_courses_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='lesson',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('lesson_title', models.CharField(max_length=50)),
                ('lesson_order', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.courses')),
            ],
        ),
    ]
