# Generated by Django 3.2.6 on 2021-08-31 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210831_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='text',
        ),
        migrations.AddField(
            model_name='feedback',
            name='Feedback',
            field=models.TextField(default=2, max_length=500),
            preserve_default=False,
        ),
    ]