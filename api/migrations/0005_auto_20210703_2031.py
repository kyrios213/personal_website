# Generated by Django 3.2.4 on 2021-07-03 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_projects_display'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projects',
            options={'verbose_name_plural': 'Projects'},
        ),
        migrations.AddField(
            model_name='profile',
            name='resume_dl',
            field=models.FileField(null=True, upload_to='resume'),
        ),
    ]
