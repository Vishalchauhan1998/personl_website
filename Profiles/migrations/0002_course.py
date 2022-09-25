# Generated by Django 2.2.28 on 2022-09-10 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_Name', models.CharField(max_length=45)),
                ('photo', models.ImageField(upload_to='Course/')),
                ('Description', models.TextField()),
                ('Category', models.CharField(choices=[('machine learning', 'Machine Learning'), ('data science & ai', 'Data Science & Ai'), ('cloud computing', 'Cloud Computing')], max_length=7)),
                ('Project_url', models.URLField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Profiles.Profile')),
            ],
        ),
    ]
