# Generated by Django 2.2.3 on 2020-02-28 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0004_auto_20200226_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voicemessage',
            name='voice_field',
            field=models.CharField(max_length=2048),
        ),
    ]
