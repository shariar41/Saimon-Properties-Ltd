# Generated by Django 3.0.2 on 2020-03-01 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spl_home', '0006_auto_20200301_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completedproject',
            name='cp_img',
            field=models.ImageField(blank=True, default='default.png', upload_to='completed_project_img'),
        ),
    ]
