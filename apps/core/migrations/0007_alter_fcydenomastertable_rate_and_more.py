# Generated by Django 4.2.6 on 2023-12-14 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_fcyexchangerate_buying_rate_deno_50_or_above_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fcydenomastertable',
            name='rate',
            field=models.DecimalField(decimal_places=4, max_digits=20),
        ),
        migrations.AlterField(
            model_name='historicalfcydenomastertable',
            name='rate',
            field=models.DecimalField(decimal_places=4, max_digits=20),
        ),
    ]
