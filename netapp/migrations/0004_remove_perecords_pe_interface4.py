# Generated by Django 4.1.7 on 2023-04-11 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netapp', '0003_alter_nerecords_carrier_vlan_mpls'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perecords',
            name='pe_interface4',
        ),
    ]