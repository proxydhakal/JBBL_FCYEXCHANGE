# Generated by Django 4.2.6 on 2023-12-05 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_historicalfcyratemaster_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fcyexchangerequestmaster',
            name='action',
            field=models.CharField(default='-', max_length=50),
        ),
        migrations.AddField(
            model_name='fcyexchangerequestmaster',
            name='depositedby',
            field=models.CharField(default='-', max_length=255),
        ),
        migrations.AddField(
            model_name='historicalfcyexchangerequestmaster',
            name='action',
            field=models.CharField(default='-', max_length=50),
        ),
        migrations.AddField(
            model_name='historicalfcyexchangerequestmaster',
            name='depositedby',
            field=models.CharField(default='-', max_length=255),
        ),
    ]