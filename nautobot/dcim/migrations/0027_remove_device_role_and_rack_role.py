# Generated by Django 3.2.16 on 2022-12-16 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dcim", "0026_rename_device_and_rack_role"),
        ("ipam", "0012_rename_ipam_roles"),
        ("virtualization", "0014_rename_virtualmachine_roles"),
        ("extras", "0065_rename_configcontext_role"),
    ]

    operations = [
        migrations.DeleteModel(
            name="DeviceRole",
        ),
        migrations.DeleteModel(
            name="RackRole",
        ),
    ]