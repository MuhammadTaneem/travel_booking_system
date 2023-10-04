# Generated by Django 4.2.5 on 2023-10-04 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tour_package', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('no_of_person', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tour_package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour_package.tourpackage')),
            ],
        ),
    ]
