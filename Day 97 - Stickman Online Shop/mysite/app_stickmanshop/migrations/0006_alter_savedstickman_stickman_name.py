# Generated by Django 5.1.2 on 2024-11-13 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_stickmanshop', '0005_alter_savedstickman_stickman_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedstickman',
            name='stickman_name',
            field=models.CharField(max_length=20),
        ),
    ]