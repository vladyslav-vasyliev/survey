# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 17:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0003_question_survey'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answerbase',
            options={'verbose_name': 'Answer', 'verbose_name_plural': 'Answers'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Question', 'verbose_name_plural': 'Questions'},
        ),
        migrations.AlterModelOptions(
            name='response',
            options={'verbose_name': 'Response', 'verbose_name_plural': 'Responses'},
        ),
        migrations.AlterModelOptions(
            name='survey',
            options={'verbose_name': 'Surveyss', 'verbose_name_plural': 'Surveys'},
        ),
    ]
