# Generated by Django 3.2.9 on 2021-12-03 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0006_alter_trailer_axle_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truck',
            name='diff_count',
            field=models.CharField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')], default='2', max_length=1),
        ),
    ]
