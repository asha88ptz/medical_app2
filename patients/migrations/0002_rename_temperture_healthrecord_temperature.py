# Generated by Django 5.0.6 on 2024-05-30 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='healthrecord',
            old_name='temperture',
            new_name='temperature',
        ),
    ]
