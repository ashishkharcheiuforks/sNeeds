# Generated by Django 2.2.3 on 2020-03-06 06:51

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('consultants', '0002_consultantprofile_user'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StorePackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='StorePackagePhase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
                ('detailed_title', models.CharField(help_text='This field is for ourselves, Feel free to add details.', max_length=1024)),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='StorePackagePhaseThrough',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('store_package', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='storePackages.StorePackage')),
                ('store_package_phase', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='storePackages.StorePackagePhase')),
            ],
            options={
                'ordering': ['order'],
                'unique_together': {('store_package', 'store_package_phase'), ('store_package', 'order')},
            },
        ),
        migrations.AddField(
            model_name='storepackage',
            name='store_package_phases',
            field=models.ManyToManyField(through='storePackages.StorePackagePhaseThrough', to='storePackages.StorePackagePhase'),
        ),
        migrations.CreateModel(
            name='SoldStorePackage',
            fields=[
                ('soldproduct_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='store.SoldProduct')),
                ('consultant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='consultants.ConsultantProfile')),
                ('store_package_detail', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='storePackages.StorePackage')),
            ],
            bases=('store.soldproduct',),
        ),
    ]
