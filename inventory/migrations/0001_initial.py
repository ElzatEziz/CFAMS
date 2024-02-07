# Generated by Django 5.0 on 2024-02-07 06:50

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("assets", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="InventoryRecord",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("inventory_date", models.DateField(verbose_name="盘点日期")),
                (
                    "actual_location",
                    models.CharField(max_length=255, verbose_name="实际位置"),
                ),
                ("status", models.CharField(max_length=50, verbose_name="状态")),
                (
                    "inventory_personnel",
                    models.CharField(max_length=255, verbose_name="盘点人员"),
                ),
                (
                    "asset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="assets.asset",
                        verbose_name="资产",
                    ),
                ),
            ],
            options={
                "verbose_name": "盘点记录",
                "verbose_name_plural": "盘点记录",
            },
        ),
    ]