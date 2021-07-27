# Generated by Django 3.1.7 on 2021-06-26 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_bio',
            new_name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user_birthdate',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user_gender',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user_image',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user_surname',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user_url',
        ),
        migrations.AddField(
            model_name='profile',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.IntegerField(choices=[(0, 'Male'), (1, 'Female')], null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default_avatar.jpg', height_field=100, upload_to='profile/', width_field=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='website',
            field=models.URLField(blank=True, default='', max_length=300),
        ),
    ]
