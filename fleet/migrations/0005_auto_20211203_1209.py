# Generated by Django 3.2.9 on 2021-12-03 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0004_alter_truck_diff_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='truck',
            name='model_no',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='truck',
            name='diff_count',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default='2'),
        ),
    ]