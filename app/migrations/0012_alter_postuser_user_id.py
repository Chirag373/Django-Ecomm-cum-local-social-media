# Generated by Django 4.1 on 2022-10-27 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_postuser_user_id_remove_registeruser_user_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postuser',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usermaster'),
        ),
    ]