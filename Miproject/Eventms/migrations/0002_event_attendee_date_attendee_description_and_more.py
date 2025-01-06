# Generated by Django 5.1.2 on 2024-12-30 05:55

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eventms', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='attendee',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.today),
        ),
        migrations.AddField(
            model_name='attendee',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='attendee',
            name='location',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='attendee',
            name='max_participants',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='attendee',
            name='organizer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='attendee_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='organiser',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='organiser',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='organiser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='organiser_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
