# Generated by Django 3.2.13 on 2022-06-17 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_builder', '0010_alter_language_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
