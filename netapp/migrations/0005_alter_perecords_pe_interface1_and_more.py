# Generated by Django 4.1.7 on 2023-04-11 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netapp', '0004_remove_perecords_pe_interface4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perecords',
            name='pe_interface1',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='perecords',
            name='pe_interface2',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='perecords',
            name='pe_interface3',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
