# Generated by Django 4.2.1 on 2023-06-28 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsonsjobbot', '0006_skill_jobsubmission_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedXlsx',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='SOWs/')),
            ],
        ),
        migrations.CreateModel(
            name='XlsxJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tonum', models.CharField(max_length=100)),
                ('posnum', models.CharField(max_length=100)),
                ('pdnum', models.CharField(max_length=100)),
                ('previous_names', models.CharField(max_length=100)),
                ('project', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('labor_cat', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=100)),
                ('clin', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('release_date', models.CharField(max_length=100)),
            ],
        ),
    ]