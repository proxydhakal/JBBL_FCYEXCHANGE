# Generated by Django 4.2.6 on 2023-12-05 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_fcyexchangerequestmaster_action_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fcyexchangerequestmaster',
            name='action',
            field=models.CharField(choices=[('APPROVED', 'APPROVED'), ('REJECTED', 'REJECTED')], default='-', max_length=50),
        ),
        migrations.AlterField(
            model_name='historicalfcyexchangerequestmaster',
            name='action',
            field=models.CharField(choices=[('APPROVED', 'APPROVED'), ('REJECTED', 'REJECTED')], default='-', max_length=50),
        ),
    ]
