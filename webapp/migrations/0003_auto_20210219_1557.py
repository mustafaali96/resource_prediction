# Generated by Django 3.1.4 on 2021-02-19 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20210219_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platform',
            name='platform_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.platformtype'),
        ),
    ]
