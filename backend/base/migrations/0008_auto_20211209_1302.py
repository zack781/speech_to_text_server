# Generated by Django 3.2.5 on 2021-12-09 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20211209_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio',
            name='file',
        ),
        migrations.AddField(
            model_name='audio',
            name='audio_file',
            field=models.FileField(blank=True, upload_to='static'),
        ),
    ]
