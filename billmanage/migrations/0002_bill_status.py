# Generated by Django 2.0.12 on 2021-03-27 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billmanage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='status',
            field=models.CharField(choices=[('P', 'Paid'), ('U', 'Unpaid')], default='P', max_length=10),
        ),
    ]
