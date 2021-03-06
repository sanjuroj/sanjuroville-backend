# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 19:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField(max_length=255)),
                ('awarder', models.CharField(max_length=255)),
                ('summary', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Basics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('label', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('website', models.CharField(max_length=255)),
                ('summary', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('postalCode', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('countryCode', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=255)),
                ('area', models.CharField(max_length=255)),
                ('studyType', models.CharField(max_length=255)),
                ('startDate', models.DateField(max_length=255)),
                ('endDate', models.DateField(max_length=255)),
                ('gpa', models.DecimalField(decimal_places=3, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='InterestKeywords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=255)),
                ('interest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Interest')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('website', models.CharField(max_length=255)),
                ('startDate', models.DateField(max_length=255)),
                ('endDate', models.DateField(max_length=255)),
                ('summary', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='JobHighlight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highlight', models.TextField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Job')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('level', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('publisher', models.CharField(max_length=255)),
                ('releaseDate', models.DateField(max_length=255)),
                ('website', models.CharField(max_length=255)),
                ('summary', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('reference', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('level', models.CharField(max_length=255)),
                ('summary', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SkillKeywords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=255)),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Skill')),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('website', models.CharField(max_length=255)),
                ('startDate', models.DateField(max_length=255)),
                ('endDate', models.DateField(max_length=255)),
                ('summary', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerHighlight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highlight', models.TextField(max_length=255)),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Volunteer')),
            ],
        ),
        migrations.AddField(
            model_name='courses',
            name='education',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Education'),
        ),
    ]
