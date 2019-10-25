# Generated by Django 2.2.6 on 2019-10-04 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ManyToManyField(related_name='events', related_query_name='event', to='events.Category'),
        ),
    ]
