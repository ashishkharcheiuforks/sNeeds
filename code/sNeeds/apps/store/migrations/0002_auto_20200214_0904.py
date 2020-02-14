# Generated by Django 2.2.3 on 2020-02-14 09:04
import random

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductAbstractClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='soldtimeslotsale',
            name='id',
        ),
        migrations.RemoveField(
            model_name='soldtimeslotsale',
            name='price',
        ),
        migrations.RemoveField(
            model_name='timeslotsale',
            name='id',
        ),
        migrations.RemoveField(
            model_name='timeslotsale',
            name='price',
        ),
        migrations.AddField(
            model_name='soldtimeslotsale',
            name='productabstractclass_ptr',
            field=models.OneToOneField(auto_created=True, default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='store.ProductAbstractClass'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timeslotsale',
            name='productabstractclass_ptr',
            field=models.OneToOneField(auto_created=True, default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='store.ProductAbstractClass'),
            preserve_default=False,
        ),
    ]
