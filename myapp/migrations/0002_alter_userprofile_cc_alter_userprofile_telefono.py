# Generated by Django 5.0.6 on 2024-07-08 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='cc',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='telefono',
            field=models.CharField(max_length=15),
        ),
    ]
