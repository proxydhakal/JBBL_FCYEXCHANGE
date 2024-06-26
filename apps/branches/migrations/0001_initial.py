# Generated by Django 4.2.6 on 2023-11-05 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BranchName', models.CharField(max_length=255)),
                ('BranchCode', models.CharField(max_length=5)),
                ('Status', models.CharField(max_length=20)),
                ('EmailStatus', models.CharField(max_length=20)),
                ('EmailAddress', models.CharField(max_length=255)),
                ('RegionalBranchName', models.CharField(blank=True, max_length=255, null=True)),
                ('IsEnteredBy', models.CharField(blank=True, max_length=255, null=True)),
                ('IsEnteredDate', models.CharField(blank=True, max_length=255, null=True)),
                ('IsEditedBy', models.CharField(blank=True, max_length=255, null=True)),
                ('IsEditedDate', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'BRANCHES',
                'verbose_name_plural': 'BRANCHES',
            },
        ),
    ]
