# Generated by Django 3.2.13 on 2022-05-08 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewbooks', '0003_rename_tel_buymodel_telefon raqam'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buymodel',
            old_name='post',
            new_name='Kitob nomi',
        ),
        migrations.RenameField(
            model_name='buymodel',
            old_name='adres',
            new_name='Manzil:',
        ),
        migrations.RenameField(
            model_name='buymodel',
            old_name='telefon raqam',
            new_name='telefon raqam:',
        ),
    ]
