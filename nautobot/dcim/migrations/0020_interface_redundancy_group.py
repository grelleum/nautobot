import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import nautobot.core.fields
import nautobot.extras.models.mixins
import nautobot.extras.models.models
import nautobot.extras.models.statuses
import nautobot.extras.utils
import taggit.managers
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("extras", "0052_configcontext_device_redundancy_groups"),
        ("ipam", "0008_prefix_vlan_vlangroup_location"),
        ("dcim", "0019_device_redundancy_group_data_migration"),
    ]

    operations = [
        migrations.CreateModel(
            name="InterfaceRedundancyGroup",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "_custom_field_data",
                    models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
                ),
                (
                    "local_context_data",
                    models.JSONField(blank=True, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True),
                ),
                ("local_context_data_owner_object_id", models.UUIDField(blank=True, default=None, null=True)),
                ("name", models.CharField(max_length=100, unique=True)),
                (
                    "slug",
                    nautobot.core.fields.AutoSlugField(blank=True, max_length=100, populate_from="name", unique=True),
                ),
                ("description", models.CharField(blank=True, max_length=200)),
                (
                    "local_context_data_owner_content_type",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        limit_choices_to=nautobot.extras.utils.FeatureQuery("config_context_owners"),
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.contenttype",
                    ),
                ),
                (
                    "local_context_schema",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="extras.configcontextschema",
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
            },
            bases=(
                models.Model,
                nautobot.extras.models.mixins.DynamicGroupMixin,
                nautobot.extras.models.mixins.NotesMixin,
                nautobot.extras.models.models.ConfigContextSchemaValidationMixin,
            ),
        ),
        migrations.CreateModel(
            name="InterfaceRedundancyGroupAssociation",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("priority", models.PositiveSmallIntegerField()),
                (
                    "group",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="dcim.interfaceredundancygroup"),
                ),
                ("interface", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="dcim.interface")),
                (
                    "primary_ip",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="interface_redundancy_primary_ip",
                        to="ipam.ipaddress",
                    ),
                ),
                (
                    "virtual_ip",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="interface_redundancy_virtual_ip",
                        to="ipam.ipaddress",
                    ),
                ),
            ],
            options={
                "ordering": ("group", "-priority"),
                "unique_together": {("group", "interface")},
            },
        ),
        migrations.AddField(
            model_name="interfaceredundancygroup",
            name="members",
            field=models.ManyToManyField(
                blank=True,
                related_name="groups",
                through="dcim.InterfaceRedundancyGroupAssociation",
                to="dcim.Interface",
            ),
        ),
        migrations.AddField(
            model_name="interfaceredundancygroup",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="dcim_interfaceredundancygroup_related",
                to="extras.status",
            ),
        ),
        migrations.AddField(
            model_name="interfaceredundancygroup",
            name="subscribers",
            field=models.ManyToManyField(blank=True, related_name="interface_redundancy_group", to="dcim.Device"),
        ),
        migrations.AddField(
            model_name="interfaceredundancygroup",
            name="tags",
            field=taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag"),
        ),
    ]
