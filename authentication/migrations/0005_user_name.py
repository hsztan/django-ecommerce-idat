# Generated by Django 3.2.5 on 2021-08-04 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_remove_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='name', max_length=200),
            preserve_default=False,
        ),
    ]
