# Generated by Django 3.2.4 on 2021-07-05 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_profile_facebook'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='code_url',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
