# Generated by Django 3.2.5 on 2021-07-31 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0005_beneficio'),
        ('interesado', '0002_alter_interesado_correo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interesado',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curso.curso'),
        ),
    ]