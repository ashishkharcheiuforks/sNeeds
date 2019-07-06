# Generated by Django 2.2.3 on 2019-07-06 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0008_auto_20190705_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSlotSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('price', models.IntegerField()),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.ConsultantProfile')),
            ],
        ),
    ]