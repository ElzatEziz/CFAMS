# Generated by Django 4.0 on 2024-02-22 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='标题')),
                ('report_type', models.CharField(choices=[('asset_summary', '资产摘要'), ('maintenance_history', '维护记录'), ('inventory_status', '库存状态'), ('disposal_record', '处置记录')], max_length=50, verbose_name='报告类型')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='生成日期')),
                ('parameters', models.TextField(blank=True, help_text='JSON格式的报告生成参数', null=True, verbose_name='报告参数')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.user', verbose_name='生成者')),
            ],
            options={
                'verbose_name': '报告',
                'verbose_name_plural': '报告',
                'db_table': 'tb_reports',
            },
        ),
    ]
