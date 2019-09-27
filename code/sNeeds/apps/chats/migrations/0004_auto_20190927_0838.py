# Generated by Django 2.2.3 on 2019-09-27 08:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0003_auto_20190927_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['.pdf', '.doc', '.docx', '.xlsx', '.xls'])]),
        ),
    ]
