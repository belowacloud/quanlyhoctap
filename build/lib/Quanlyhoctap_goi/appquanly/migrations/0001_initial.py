# Generated by Django 2.2.6 on 2019-12-23 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deadline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Deadline_name', models.CharField(max_length=200, verbose_name='deadline of subject')),
                ('description', models.CharField(max_length=200, verbose_name='description')),
                ('date', models.DateTimeField(default=0, verbose_name='date of deadline')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject_name', models.CharField(max_length=200, verbose_name='subject name')),
                ('Subject_code', models.CharField(max_length=200, verbose_name='subject code')),
                ('Room_code', models.CharField(max_length=200, verbose_name='class name')),
                ('document', models.CharField(max_length=2000, verbose_name='document needed')),
                ('date_exam', models.DateTimeField(default=0, verbose_name='date of exam')),
            ],
        ),
    ]
