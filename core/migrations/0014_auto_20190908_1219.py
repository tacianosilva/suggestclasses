# Generated by Django 2.1.5 on 2019-09-08 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20190908_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='turno',
            field=models.CharField(max_length=50),
        ),
    ]
