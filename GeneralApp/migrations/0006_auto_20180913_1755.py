# Generated by Django 2.1.1 on 2018-09-13 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GeneralApp', '0005_auto_20180913_1751'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='note',
            new_name='Note',
        ),
        migrations.AddField(
            model_name='person',
            name='Time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
