# Generated by Django 2.1.3 on 2019-03-10 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20190310_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='public_classes',
            field=models.ManyToManyField(blank=True, to='classes.PublicClass'),
        ),
    ]
