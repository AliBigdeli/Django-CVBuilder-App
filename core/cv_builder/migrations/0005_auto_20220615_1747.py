# Generated by Django 3.2.13 on 2022-06-15 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_builder', '0004_auto_20220615_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationexperience',
            name='start_month',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='educationexperience',
            name='start_year',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
