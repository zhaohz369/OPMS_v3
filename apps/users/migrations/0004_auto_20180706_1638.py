# Generated by Django 2.0.6 on 2018-07-06 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180706_1545'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermanageuserrecord',
            old_name='opration',
            new_name='operation',
        ),
    ]
