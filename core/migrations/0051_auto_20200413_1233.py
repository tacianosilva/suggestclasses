# Generated by Django 3.0.4 on 2020-04-13 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0050_discente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discente',
            name='matricula',
            field=models.IntegerField(unique=True),
        ),
    ]
