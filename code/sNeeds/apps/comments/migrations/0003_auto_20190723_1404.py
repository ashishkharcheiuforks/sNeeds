# Generated by Django 2.2.3 on 2019-07-23 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_admincomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admincomment',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_reply', to='comments.Comment'),
        ),
    ]