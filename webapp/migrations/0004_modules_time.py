# Generated by Django 3.1.4 on 2021-02-26 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20210219_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='modules',
            name='time',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
