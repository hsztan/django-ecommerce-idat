# Generated by Django 3.2.5 on 2021-07-28 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0002_auto_20210727_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.CharField(max_length=150)),
                ('frecuencia', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Horario',
                'verbose_name_plural': 'Horarios',
                'db_table': 'horario',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.AddField(
            model_name='curso',
            name='horarios',
            field=models.ManyToManyField(to='curso.Horario'),
        ),
    ]
