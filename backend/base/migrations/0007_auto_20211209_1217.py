# Generated by Django 3.2.5 on 2021-12-09 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20211209_1101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio',
            name='audio_file',
        ),
        migrations.RemoveField(
            model_name='audio',
            name='file_name',
        ),
        migrations.RemoveField(
            model_name='audio',
            name='image',
        ),
        migrations.AddField(
            model_name='audio',
            name='file',
            field=models.FileField(default='example.wav', upload_to=''),
        ),
    ]
