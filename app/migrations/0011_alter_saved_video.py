# Generated by Django 4.0.6 on 2022-08-14 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_saved_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saved',
            name='video',
            field=models.CharField(max_length=500),
        ),
    ]
