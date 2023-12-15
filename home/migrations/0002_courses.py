# Generated by Django 4.2.7 on 2023-12-05 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=255)),
                ('course_fee', models.CharField(max_length=255)),
                ('course_description', models.TextField()),
                ('course_type', models.BooleanField(choices=[(True, 'Paid'), (False, 'Unpaid')], default=False)),
                ('course_status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='inactive', max_length=10)),
                ('create_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]