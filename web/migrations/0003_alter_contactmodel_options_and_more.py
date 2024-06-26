# Generated by Django 5.0.6 on 2024-05-18 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_detailsoption_standartoption_servicemodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactmodel',
            options={'verbose_name': 'Contact Message', 'verbose_name_plural': 'Contact Messages'},
        ),
        migrations.AlterModelOptions(
            name='detailsoption',
            options={'verbose_name': 'Details Option', 'verbose_name_plural': 'Details Options'},
        ),
        migrations.AlterModelOptions(
            name='servicemodel',
            options={'verbose_name': 'Service', 'verbose_name_plural': 'Services'},
        ),
        migrations.AlterModelOptions(
            name='serviceoption',
            options={'verbose_name': 'Service Option', 'verbose_name_plural': 'Service Options'},
        ),
        migrations.AlterModelOptions(
            name='standartoption',
            options={'verbose_name': 'Standard Option', 'verbose_name_plural': 'Standard Options'},
        ),
    ]
