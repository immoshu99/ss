# Generated by Django 3.1.7 on 2021-10-15 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20211015_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=11),
        ),
    ]