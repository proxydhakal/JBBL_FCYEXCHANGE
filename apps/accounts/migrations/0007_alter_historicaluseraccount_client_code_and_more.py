# Generated by Django 4.2.6 on 2023-12-06 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_userdetails_historicaluserdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaluseraccount',
            name='client_code',
            field=models.CharField(blank=True, default='-', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='client_code',
            field=models.CharField(blank=True, default='-', max_length=20, null=True),
        ),
    ]
