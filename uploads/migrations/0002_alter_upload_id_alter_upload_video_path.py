# Generated by Django 4.0.6 on 2022-08-03 21:56

from django.db import migrations, models
import uploads.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='upload',
            name='video_path',
            field=models.FileField(upload_to='videos', validators=[uploads.models.validate_video], verbose_name='Video'),
        ),
    ]
