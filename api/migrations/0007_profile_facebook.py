# Generated by Django 3.2.4 on 2021-07-04 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_profile_resume_dl'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='facebook',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
