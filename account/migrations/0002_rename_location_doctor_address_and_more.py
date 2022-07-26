# Generated by Django 4.0.6 on 2022-07-24 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='location',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='designation',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='doctor',
            name='profile_photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='patient',
            name='profile_photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
