# Generated by Django 4.0.5 on 2022-07-02 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewbooks', '0016_engbooksmodel_user_engbooksmodel_whose_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rusbuymodel',
            name='user',
        ),
        migrations.RemoveField(
            model_name='rusbuymodel',
            name='whose',
        ),
        migrations.RemoveField(
            model_name='uzbuymodel',
            name='user',
        ),
        migrations.RemoveField(
            model_name='uzbuymodel',
            name='whose',
        ),
        migrations.AddField(
            model_name='rusbooksmodel',
            name='user',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='rusbooksmodel',
            name='whose',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='uzbbooksmodel',
            name='user',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='uzbbooksmodel',
            name='whose',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
