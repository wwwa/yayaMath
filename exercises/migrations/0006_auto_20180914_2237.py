# Generated by Django 2.0 on 2018-09-14 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0005_record'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='is_rigtht',
            new_name='is_right',
        ),
    ]
