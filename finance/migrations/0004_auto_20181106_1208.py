# Generated by Django 2.1 on 2018-11-06 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_auto_20181106_1205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accounts',
            old_name='type',
            new_name='acc_type',
        ),
    ]