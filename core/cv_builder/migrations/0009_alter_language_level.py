# Generated by Django 3.2.13 on 2022-06-16 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_builder', '0008_auto_20220616_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='level',
            field=models.IntegerField(choices=[(1, 'Native'), (2, 'Beginner'), (3, 'Elementary'), (4, 'Intermediate'), (5, 'Upper intermediate'), (6, 'Advanced'), (7, 'Proficient')], default=1),
        ),
    ]