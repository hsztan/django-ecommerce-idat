# Generated by Django 3.2.5 on 2021-08-02 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0006_alter_beneficio_detalle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]