# Generated by Django 4.0 on 2024-02-14 06:56

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaintenanceRecord',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('maintenance_date', models.DateField(verbose_name='维护日期')),
                ('maintenance_type', models.CharField(choices=[('routine_check', '例行检查'), ('emergency_repair', '紧急维修'), ('part_replacement', '零件更换')], max_length=50, verbose_name='维护类型')),
                ('cost', models.FloatField(verbose_name='成本')),
                ('result', models.TextField(verbose_name='结果')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.asset', verbose_name='关联资产')),
            ],
            options={
                'verbose_name': '维护记录',
                'verbose_name_plural': '维护记录',
            },
        ),
    ]
