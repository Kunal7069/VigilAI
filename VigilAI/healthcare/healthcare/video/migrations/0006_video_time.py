# Generated by Django 3.2.16 on 2023-05-15 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0005_alter_video_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='time',
            field=models.CharField(default=12345, max_length=50),
            preserve_default=False,
        ),
    ]
