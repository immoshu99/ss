# Generated by Django 3.1.7 on 2021-10-08 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20211008_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='bloodgroup',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='myapp.bloodgroup'),
        ),
    ]
