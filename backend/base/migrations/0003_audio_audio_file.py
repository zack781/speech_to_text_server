# Generated by Django 3.2.5 on 2021-11-04 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_audio_audio_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
