# Generated by Django 2.0.7 on 2018-09-21 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pontuacoes', '0002_auto_20180921_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividadealuno',
            name='agilidade',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='atividadealuno',
            name='perfeccionismo',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='atividadealuno',
            name='precisao',
            field=models.BooleanField(default=False),
        ),
    ]
