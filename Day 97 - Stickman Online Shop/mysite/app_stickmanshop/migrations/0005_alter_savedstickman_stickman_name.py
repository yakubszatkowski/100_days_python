# Generated by Django 5.1.2 on 2024-11-13 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_stickmanshop', '0004_alter_savedstickman_stickman_clothes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedstickman',
            name='stickman_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]