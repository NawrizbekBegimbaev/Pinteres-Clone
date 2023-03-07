# Generated by Django 4.0 on 2023-03-04 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pinteres', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pinteres.customuser'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='nameuser',
            field=models.CharField(max_length=200),
        ),
    ]
