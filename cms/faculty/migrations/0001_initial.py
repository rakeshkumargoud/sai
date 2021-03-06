# Generated by Django 3.0.5 on 2020-06-05 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyModel',
            fields=[
                ('idno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('contactno', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('salary', models.FloatField()),
                ('subject', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
