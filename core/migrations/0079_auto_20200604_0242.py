# Generated by Django 3.0.6 on 2020-06-04 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0078_vototurma'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='vototurma',
            unique_together={('enquete', 'discente', 'componente')},
        ),
    ]
