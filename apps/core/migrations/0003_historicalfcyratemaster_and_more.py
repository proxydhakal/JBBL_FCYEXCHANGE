# Generated by Django 4.2.6 on 2023-12-03 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_fcyexchangerequestmaster_remarks'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalFCYRateMaster',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('user', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical FCY RATE MASTER',
                'verbose_name_plural': 'historical FCY RATE MASTERS',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalFCYExchangeRequestMaster',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('refrenceid', models.CharField(db_index=True, max_length=20)),
                ('date', models.DateField()),
                ('preferredBranch', models.CharField(max_length=10)),
                ('totalEquivalentNPR', models.DecimalField(decimal_places=2, max_digits=20)),
                ('totalEquivalentNPRToWords', models.CharField(max_length=300)),
                ('status', models.CharField(max_length=50)),
                ('remarks', models.TextField(default='-')),
                ('enteredBy', models.CharField(max_length=255)),
                ('enterDate', models.DateTimeField()),
                ('updatedBy', models.CharField(max_length=255)),
                ('updateDate', models.DateTimeField()),
                ('deletedBy', models.CharField(max_length=255)),
                ('deletedDate', models.DateTimeField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical FCY EXCHANGE REQUEST MASTER TABLE',
                'verbose_name_plural': 'historical FCY EXCHANGE REQUEST MASTER TABLES',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalFCYExchangeRate',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('masterid', models.IntegerField()),
                ('currency_code', models.CharField(max_length=10)),
                ('currency', models.CharField(max_length=255)),
                ('currency_unit', models.CharField(max_length=50)),
                ('buying_rate_deno_50_or_less', models.DecimalField(decimal_places=2, max_digits=10)),
                ('buying_rate_deno_50_or_above', models.DecimalField(decimal_places=2, max_digits=10)),
                ('selling_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('premium_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical FCY EXCHANGE RATE',
                'verbose_name_plural': 'historical FCY EXCHANGE RATES',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalFCYDenoMasterTable',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('masterid', models.IntegerField()),
                ('currency', models.CharField(max_length=255)),
                ('deno', models.IntegerField()),
                ('unit', models.IntegerField()),
                ('rate', models.DecimalField(decimal_places=2, max_digits=20)),
                ('equivalentNPR', models.DecimalField(decimal_places=2, max_digits=20)),
                ('status', models.CharField(max_length=50)),
                ('enteredBy', models.CharField(max_length=255)),
                ('enterDate', models.DateTimeField()),
                ('updatedBy', models.CharField(max_length=255)),
                ('updateDate', models.DateTimeField()),
                ('deletedBy', models.CharField(max_length=255)),
                ('deletedDate', models.DateTimeField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical FCY DENO MASTER TABLE',
                'verbose_name_plural': 'historical FCY DENO MASTER TABLES',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCurrencyTable',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('cyc_code', models.CharField(max_length=10)),
                ('cyc_desc', models.CharField(max_length=255)),
                ('cyc_desc_long', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical CURRENCY TABLE',
                'verbose_name_plural': 'historical CURRENCY TABLES',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
