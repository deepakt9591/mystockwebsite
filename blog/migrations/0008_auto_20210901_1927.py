# Generated by Django 3.2.6 on 2021-09-01 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_rename_text_feedback_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='Name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='Feedback',
            new_name='text',
        ),
    ]
