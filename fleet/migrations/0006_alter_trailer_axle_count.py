# Generated by Django 3.2.9 on 2021-12-03 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0005_auto_20211203_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trailer',
            name='axle_count',
            field=models.IntegerField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four'), ('5', 'Five'), ('6', 'Six')], default='3'),
        ),
    ]
