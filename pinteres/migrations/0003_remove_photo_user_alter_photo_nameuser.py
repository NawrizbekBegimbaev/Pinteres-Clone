# Generated by Django 4.0 on 2023-03-04 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinteres', '0002_photo_user_alter_photo_nameuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='user',
        ),
        migrations.AlterField(
            model_name='photo',
            name='nameuser',
            field=models.CharField(blank=True, default='settings.AUTH_USER_MODEL.name', max_length=200, null=True),
        ),
    ]
