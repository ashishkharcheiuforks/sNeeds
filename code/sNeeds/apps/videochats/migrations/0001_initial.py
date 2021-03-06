# Generated by Django 2.2.3 on 2020-02-29 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.IntegerField(blank=True, null=True)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('consultant_id', models.IntegerField(blank=True, null=True)),
                ('user_login_url', models.URLField(blank=True, max_length=1024)),
                ('consultant_login_url', models.URLField(blank=True, max_length=1024)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('sold_time_slot', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.SoldTimeSlotSale')),
            ],
        ),
    ]
