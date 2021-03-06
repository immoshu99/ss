# Generated by Django 3.1.7 on 2021-10-29 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0013_auto_20211030_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='blood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.bloodgroup'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.city'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_donation',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='profile',
            name='thana',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.thana'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
