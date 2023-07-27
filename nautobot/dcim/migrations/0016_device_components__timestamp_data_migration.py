# Generated by Django 3.1.14 on 2022-03-19 23:21

from django.db import migrations


# Models that need to share their parent's timestamps.
COMPONENT_MODELS = [
    "dcim.consoleport",
    "dcim.consoleporttemplate",
    "dcim.consoleserverport",
    "dcim.consoleserverporttemplate",
    "dcim.devicebay",
    "dcim.devicebaytemplate",
    "dcim.frontport",
    "dcim.frontporttemplate",
    "dcim.interface",
    "dcim.interfacetemplate",
    "dcim.inventoryitem",
    "dcim.poweroutlet",
    "dcim.poweroutlettemplate",
    "dcim.powerport",
    "dcim.powerporttemplate",
    "dcim.rearport",
    "dcim.rearporttemplate",
]


def populate_device_component_timestamps(apps, schema_editor):
    """
    Set created/last_updated fields of existing components to None, rather than the time of the migration.
    """
    for model_path in COMPONENT_MODELS:
        model = apps.get_model(model_path)
        model.objects.all().update(created=None, last_updated=None)


class Migration(migrations.Migration):
    dependencies = [
        ("dcim", "0015_device_components__changeloggedmodel"),
    ]

    operations = [
        migrations.RunPython(populate_device_component_timestamps, migrations.RunPython.noop),
    ]
