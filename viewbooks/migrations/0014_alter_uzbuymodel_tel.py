# Generated by Django 4.0.5 on 2022-07-01 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewbooks', '0013_engbooksmodel_barcode_rusbooksmodel_barcode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uzbuymodel',
            name='tel',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
