# Generated by Django 2.2.14 on 2021-03-19 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_package_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='day2',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='day3',
            field=models.TextField(blank=True, null=True),
        ),
    ]
