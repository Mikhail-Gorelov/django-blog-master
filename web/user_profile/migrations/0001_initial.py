# Generated by Django 3.2.9 on 2022-01-04 18:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.IntegerField(choices=[(0, 'Male'), (1, 'Female')], null=True)),
                ('image', models.ImageField(default='default_avatar.jpg', upload_to='profile/')),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('bio', models.TextField(default='', help_text='Bio', max_length=2000)),
                ('website', models.URLField(blank=True, default='', max_length=300)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
