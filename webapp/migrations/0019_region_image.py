# Generated by Django 3.1.4 on 2021-03-17 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0018_auto_20210315_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/Region'),
        ),
    ]