# Generated by Django 4.2.5 on 2023-10-04 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('Customer', 'customer'), ('Counter', 'counter'), ('Manager', 'manager')], max_length=20),
        ),
    ]
