# Generated by Django 3.2.13 on 2022-06-15 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_builder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='order',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='affiliate',
            name='order',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='certification',
            name='order',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='educationexperience',
            name='order',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='language',
            name='order',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='link',
            name='order',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='order',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='order',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
