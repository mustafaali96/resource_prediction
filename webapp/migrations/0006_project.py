# Generated by Django 3.1.4 on 2021-03-02 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20210226_1136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cost', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('assigned_designation', models.ManyToManyField(blank=True, null=True, related_name='assigned_designation', to='webapp.Designation')),
                ('modules', models.ManyToManyField(related_name='Project_modules', to='webapp.Modules')),
                ('platform', models.ManyToManyField(related_name='Project_platform', to='webapp.Platform')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.region')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.projecttemplate')),
            ],
        ),
    ]
