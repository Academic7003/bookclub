# Generated by Django 3.2.13 on 2022-05-08 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewbooks', '0004_auto_20220508_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buymodel',
            name='Kitob nomi',
        ),
        migrations.AddField(
            model_name='buymodel',
            name='Kitob nomi:',
            field=models.ForeignKey(default=555, on_delete=django.db.models.deletion.CASCADE, to='viewbooks.uzbbooksmodel'),
            preserve_default=False,
        ),
    ]
