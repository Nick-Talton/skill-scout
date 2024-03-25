# Generated by Django 4.2.1 on 2023-06-26 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsonsjobbot', '0005_jobsubmission'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='jobsubmission',
            name='skills',
            field=models.ManyToManyField(to='parsonsjobbot.skill'),
        ),
    ]
