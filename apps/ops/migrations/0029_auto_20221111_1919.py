# Generated by Django 3.2.14 on 2022-11-11 11:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assets', '0111_alter_automationexecution_status'),
        ('ops', '0028_celerytask_last_published_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('created_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Created by')),
                ('updated_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Updated by')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, null=True, verbose_name='Name')),
                ('instant', models.BooleanField(default=False)),
                ('args', models.CharField(blank=True, default='', max_length=1024, null=True, verbose_name='Args')),
                ('module', models.CharField(choices=[('shell', 'Shell'), ('win_shell', 'Powershell')], default='shell', max_length=128, null=True, verbose_name='Module')),
                ('type', models.CharField(choices=[('adhoc', 'Adhoc'), ('playbook', 'Playbook')], default='adhoc', max_length=128, verbose_name='Type')),
                ('runas', models.CharField(default='root', max_length=128, verbose_name='Runas')),
                ('runas_policy', models.CharField(choices=[('privileged_only', 'Privileged Only'), ('privileged_first', 'Privileged First'), ('skip', 'Skip')], default='skip', max_length=128, verbose_name='Runas policy')),
                ('assets', models.ManyToManyField(to='assets.Asset', verbose_name='Assets')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JobExecution',
            fields=[
                ('created_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Created by')),
                ('updated_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Updated by')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('task_id', models.UUIDField(null=True)),
                ('status', models.CharField(default='running', max_length=16, verbose_name='Status')),
                ('result', models.JSONField(blank=True, null=True, verbose_name='Result')),
                ('summary', models.JSONField(default=dict, verbose_name='Summary')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('date_start', models.DateTimeField(db_index=True, null=True, verbose_name='Date start')),
                ('date_finished', models.DateTimeField(null=True, verbose_name='Date finished')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='executions', to='ops.job')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='playbooktemplate',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='adhoc',
            name='account',
        ),
        migrations.RemoveField(
            model_name='adhoc',
            name='account_policy',
        ),
        migrations.RemoveField(
            model_name='adhoc',
            name='assets',
        ),
        migrations.RemoveField(
            model_name='adhoc',
            name='crontab',
        ),
        migrations.RemoveField(
            model_name='adhoc',
            name='date_last_run',
        ),
        migrations.RemoveField(
            model_name='adhoc',
            name='interval',
        ),
        migrations.RemoveField(
            model_name='adhoc',
            name='is_periodic',
        ),
        migrations.RemoveField(
            model_name='adhoc',
            name='last_execution',
        ),
        migrations.RemoveField(
            model_name='adhoc',
            name='org_id',
        ),
        migrations.RemoveField(
            model_name='playbook',
            name='account',
        ),
        migrations.RemoveField(
            model_name='playbook',
            name='account_policy',
        ),
        migrations.RemoveField(
            model_name='playbook',
            name='assets',
        ),
        migrations.RemoveField(
            model_name='playbook',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='playbook',
            name='crontab',
        ),
        migrations.RemoveField(
            model_name='playbook',
            name='date_last_run',
        ),
        migrations.RemoveField(
            model_name='playbook',
            name='interval',
        ),
        migrations.RemoveField(
            model_name='playbook',
            name='is_periodic',
        ),
        migrations.RemoveField(
            model_name='playbook',
            name='last_execution',
        ),
        migrations.RemoveField(
            model_name='playbook',
            name='org_id',
        ),
        migrations.RemoveField(
            model_name='playbook',
            name='template',
        ),
        migrations.AlterField(
            model_name='adhoc',
            name='module',
            field=models.CharField(choices=[('shell', 'Shell'), ('win_shell', 'Powershell')], default='shell', max_length=128, verbose_name='Module'),
        ),
        migrations.AlterField(
            model_name='playbook',
            name='name',
            field=models.CharField(max_length=128, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='playbook',
            name='path',
            field=models.FileField(upload_to='playbooks/'),
        ),
        migrations.DeleteModel(
            name='PlaybookExecution',
        ),
        migrations.DeleteModel(
            name='PlaybookTemplate',
        ),
        migrations.AddField(
            model_name='job',
            name='playbook',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ops.playbook', verbose_name='Playbook'),
        ),
    ]