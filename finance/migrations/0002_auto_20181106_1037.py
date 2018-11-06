# Generated by Django 2.1 on 2018-11-06 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounts',
            name='balance',
        ),
        migrations.AlterField(
            model_name='accounts',
            name='type',
            field=models.CharField(choices=[('credit', 'Credit'), ('debit', 'Debit')], max_length=10),
        ),
    ]