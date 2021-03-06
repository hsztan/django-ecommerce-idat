# Generated by Django 3.2.5 on 2021-07-31 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0004_curso_precio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=150)),
                ('detalle', models.TextField()),
                ('icono', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Beneficio',
                'verbose_name_plural': 'Beneficios',
                'db_table': 'beneficio',
                'ordering': ['-updated_at'],
            },
        ),
    ]
