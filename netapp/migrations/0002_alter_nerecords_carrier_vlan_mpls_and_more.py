# Generated by Django 4.1.7 on 2023-04-11 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nerecords',
            name='carrier_vlan_mpls',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='nerecords',
            name='comments',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='nerecords',
            name='device_interfaces',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='perecords',
            name='pe_interface2',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='perecords',
            name='pe_interface3',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='perecords',
            name='pe_interface4',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='perecords',
            name='pe_ip2',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
