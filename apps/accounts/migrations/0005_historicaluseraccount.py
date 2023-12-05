# Generated by Django 4.2.6 on 2023-12-03 07:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_useraccount_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalUserAccount',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('role', models.IntegerField(choices=[(0, 'SUPER_ADMIN'), (1, 'USER'), (2, 'BRANCH_STAFF')], default=1)),
                ('email', models.EmailField(db_index=True, max_length=254)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('client_code', models.CharField(blank=True, default='-', max_length=10, null=True)),
                ('branch', models.CharField(blank=True, default='-', max_length=10, null=True)),
                ('profile_image', models.TextField(default='profile_pics/default.png', max_length=100)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_email_verified', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('INACTIVE', 'Inactive'), ('ACTIVE', 'Active'), ('DELETED', 'Deleted')], default='ACTIVE', max_length=50)),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('company', models.CharField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('location', models.CharField(blank=True, default='-', max_length=255, null=True)),
                ('dob', models.DateField(blank=True, default='2022-02-02', null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical USER ACCOUNT',
                'verbose_name_plural': 'historical USER ACCOUNTS',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
