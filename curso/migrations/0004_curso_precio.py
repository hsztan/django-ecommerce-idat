# Generated by Django 3.2.5 on 2021-07-29 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0003_auto_20210727_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=450.2, max_digits=6),
            preserve_default=False,
        ),
    ]