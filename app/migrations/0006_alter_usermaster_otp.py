# Generated by Django 4.1.2 on 2022-10-23 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_usermaster_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermaster',
            name='Otp',
            field=models.IntegerField(default=True),
        ),
    ]