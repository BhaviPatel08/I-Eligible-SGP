# Generated by Django 4.1.4 on 2023-03-27 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_rename_clg_cgpa_scst_college_clg_cgpa_sc_st'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='clg_official_link',
            field=models.CharField(default='www.youtube.com', max_length=300),
        ),
        migrations.AddField(
            model_name='school',
            name='scl_official_link',
            field=models.CharField(default='www.youtube.com', max_length=300),
        ),
    ]
