# Generated by Django 3.2.5 on 2021-08-03 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_cupon_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.cupon'),
        ),
    ]
