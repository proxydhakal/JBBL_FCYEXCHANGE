# Generated by Django 4.2.6 on 2023-11-05 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branches',
            name='BranchCode',
            field=models.CharField(max_length=10),
        ),
    ]
