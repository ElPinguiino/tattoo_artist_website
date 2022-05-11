# Generated by Django 4.0.4 on 2022-04-26 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='date',
            new_name='scheduled_date',
        ),
        migrations.RemoveField(
            model_name='client',
            name='bookings',
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=20),
        ),
        migrations.AlterField(
            model_name='client',
            name='first_name',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
