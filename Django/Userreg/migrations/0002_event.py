# Generated by Django 2.2.3 on 2020-01-14 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userreg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('venue', models.CharField(max_length=200)),
                ('date', models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.')),
                ('time', models.TimeField(help_text='Please use the following format: <em>HH:MM:SS<em>')),
                ('category', models.CharField(max_length=50)),
                ('num_of_attendees', models.PositiveIntegerField(blank=True, default=0)),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
                'ordering': ['date', 'time'],
            },
        ),
    ]
