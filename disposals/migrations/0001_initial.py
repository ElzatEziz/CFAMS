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
            name="DisposalRecord",
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
                ("disposal_date", models.DateField(verbose_name="处置日期")),
                (
                    "disposal_method",
                    models.CharField(
                        choices=[("sale", "售出"), ("donation", "捐赠"), ("scrap", "废弃")],
                        max_length=50,
                        verbose_name="处置方式",
                    ),
                ),
                (
                    "recipient",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="接收方"
                    ),
                ),
                ("cost_or_revenue", models.FloatField(verbose_name="相关成本或收入")),
                (
                    "asset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="assets.asset",
                        verbose_name="处置资产",
                    ),
                ),
            ],
            options={
                "verbose_name": "资产处置记录",
                "verbose_name_plural": "资产处置记录",
            },
        ),
    ]
