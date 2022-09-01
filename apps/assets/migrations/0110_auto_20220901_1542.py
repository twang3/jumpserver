# Generated by Django 3.2.14 on 2022-09-01 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0109_auto_20220901_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='platform',
            name='create_account_enabled',
            field=models.BooleanField(default=False, verbose_name='Create account enabled'),
        ),
        migrations.AddField(
            model_name='platform',
            name='create_account_method',
            field=models.TextField(blank=True, max_length=32, null=True, verbose_name='Create account method'),
        ),
        migrations.AddField(
            model_name='platform',
            name='gather_accounts_enabled',
            field=models.BooleanField(default=False, verbose_name='Gather facts enabled'),
        ),
        migrations.AddField(
            model_name='platform',
            name='gather_accounts_method',
            field=models.TextField(blank=True, max_length=32, null=True, verbose_name='Gather facts method'),
        ),
        migrations.AddField(
            model_name='platform',
            name='gather_facts_enabled',
            field=models.BooleanField(default=False, verbose_name='Gather facts enabled'),
        ),
        migrations.AddField(
            model_name='platform',
            name='gather_facts_method',
            field=models.TextField(blank=True, max_length=32, null=True, verbose_name='Gather facts method'),
        ),
    ]
