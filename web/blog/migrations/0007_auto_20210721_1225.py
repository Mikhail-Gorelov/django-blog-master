# Generated by Django 3.1.7 on 2021-07-21 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210721_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='parent_comment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.comment'),
        ),
    ]
