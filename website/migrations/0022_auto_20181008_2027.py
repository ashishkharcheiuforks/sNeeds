# Generated by Django 2.0.5 on 2018-10-08 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_booklet_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booklet',
            name='topic',
        ),
        migrations.AddField(
            model_name='booklet',
            name='topic',
            field=models.ManyToManyField(related_name='booklets', to='website.BookletTopic'),
        ),
    ]