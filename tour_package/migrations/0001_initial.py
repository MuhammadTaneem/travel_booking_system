# Generated by Django 4.2.5 on 2023-10-04 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TourPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image_1', models.ImageField(upload_to='')),
                ('image_2', models.ImageField(upload_to='')),
                ('image_3', models.ImageField(upload_to='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('daily_limit', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('location', models.CharField()),
                ('duration', models.CharField()),
                ('policy', models.CharField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
