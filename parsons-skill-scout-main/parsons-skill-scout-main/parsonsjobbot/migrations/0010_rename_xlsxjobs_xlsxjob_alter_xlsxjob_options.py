# Generated by Django 4.2.1 on 2023-06-28 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parsonsjobbot', '0009_alter_xlsxjobs_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='XlsxJobs',
            new_name='XlsxJob',
        ),
        migrations.AlterModelOptions(
            name='xlsxjob',
            options={},
        ),
    ]
