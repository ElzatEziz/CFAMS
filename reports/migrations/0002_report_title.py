# Generated by Django 4.2.10 on 2024-02-07 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='title',
            field=models.CharField(max_length=100, null=True, verbose_name='标题'),
        ),
    ]
