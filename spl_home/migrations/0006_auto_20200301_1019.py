# Generated by Django 3.0.2 on 2020-03-01 10:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('spl_home', '0005_auto_20200301_0939'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('unit_size', models.CharField(max_length=100)),
                ('completion_date', models.DateField()),
                ('cp_img', models.ImageField(blank=True, default='default.png', upload_to='ongoing_project_img')),
                ('date_posted', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='upcomingproject',
            name='ucp_img',
            field=models.ImageField(blank=True, default='http://placehold.it/700x400', upload_to='upcoming_project_img'),
        ),
    ]
