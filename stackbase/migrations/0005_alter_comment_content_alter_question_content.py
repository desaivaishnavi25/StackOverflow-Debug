# Generated by Django 4.2.2 on 2023-06-30 03:00

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stackbase', '0004_question_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
