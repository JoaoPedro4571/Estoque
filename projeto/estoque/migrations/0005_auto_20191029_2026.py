# Generated by Django 2.2.5 on 2019-10-29 23:26

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0004_protocoloentrega_protocoloentregaitens'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='protocoloentrega',
            name='data',
        ),
        migrations.AddField(
            model_name='protocoloentrega',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2019, 10, 29, 23, 26, 37, 541053, tzinfo=utc), verbose_name='criado em'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='protocoloentrega',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modificado em'),
        ),
    ]
