# Generated by Django 2.2.3 on 2019-08-16 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videochats', '0005_auto_20190816_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='user1_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='user2_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]