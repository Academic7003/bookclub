# Generated by Django 4.0.5 on 2022-06-30 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewbooks', '0012_engbuymodel_created_time_rusbuymodel_created_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='engbooksmodel',
            name='barcode',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rusbooksmodel',
            name='barcode',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='uzbbooksmodel',
            name='barcode',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
    ]
