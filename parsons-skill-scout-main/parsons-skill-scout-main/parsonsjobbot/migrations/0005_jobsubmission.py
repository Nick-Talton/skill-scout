# Generated by Django 4.2.1 on 2023-06-26 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsonsjobbot', '0004_candidate_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_id', models.CharField(max_length=50)),
                ('position_description', models.IntegerField()),
                ('skill_level', models.IntegerField()),
                ('job_title', models.CharField(max_length=100)),
            ],
        ),
    ]
