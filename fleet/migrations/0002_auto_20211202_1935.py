# Generated by Django 3.2.9 on 2021-12-02 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trailer',
            name='date_commissioned',
        ),
        migrations.RemoveField(
            model_name='truck',
            name='date_commissioned',
        ),
        migrations.AddField(
            model_name='trailer',
            name='tare_weight',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='truck',
            name='tare_weight',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trailer',
            name='make',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='truck',
            name='fuel_type',
            field=models.CharField(choices=[('Diesel', 'Diesel'), ('Petrol', 'Petrol'), ('Electric', 'Electric'), ('Hybrid', 'Hybrid'), ('Hydrogen', 'Hydrogen')], default='Diesel', max_length=10),
        ),
        migrations.AlterField(
            model_name='truck',
            name='make',
            field=models.CharField(max_length=30),
        ),
    ]
