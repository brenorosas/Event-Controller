# Generated by Django 3.1.7 on 2021-04-03 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evcontrol', '0003_guest_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(default=1, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
