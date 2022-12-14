# Generated by Django 4.1.2 on 2022-10-23 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_register_email_remove_register_mobile_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registeruser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=50)),
                ('Lastname', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='usermaster',
            name='is_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='usermaster',
            name='is_updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.DeleteModel(
            name='Register',
        ),
        migrations.AddField(
            model_name='registeruser',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usermaster'),
        ),
    ]
