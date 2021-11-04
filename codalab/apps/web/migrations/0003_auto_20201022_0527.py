# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-22 05:27
from __future__ import unicode_literals

import apps.web.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import storages.backends.s3boto3
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_submissioncomputedscore_weights'),
    ]

    operations = [
        migrations.AddField(
            model_name='competitiondefbundle',
            name='competition',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bundle', to='web.Competition'),
        ),
        migrations.AddField(
            model_name='competitionphase',
            name='delete_submissions_except_best_and_last',
            field=models.BooleanField(default=False, verbose_name='Delete all submissions except latest and or best. (Use with caution)'),
        ),
        migrations.AddField(
            model_name='competitionphase',
            name='max_submission_size',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)], verbose_name='Max submission size in megabytes. (0 for disabled)'),
        ),
        migrations.AddField(
            model_name='competitionphase',
            name='participant_max_storage_use',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(500000), django.core.validators.MinValueValidator(0)], verbose_name='Max megabyte usage for each participant. (0 for disabled)'),
        ),
        migrations.AddField(
            model_name='competitionsubmission',
            name='sub_size',
            field=models.BigIntegerField(default=0),
        ),
    ]
