# Generated by Django 3.2.14 on 2022-10-27 03:25

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0107_auto_20221019_1115'),
        ('terminal', '0053_auto_20220830_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applet',
            fields=[
                ('created_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Created by')),
                ('updated_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Updated by')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.SlugField(max_length=128, unique=True, verbose_name='Name')),
                ('display_name', models.CharField(max_length=128, verbose_name='Display name')),
                ('version', models.CharField(max_length=16, verbose_name='Version')),
                ('author', models.CharField(max_length=128, verbose_name='Author')),
                ('type', models.CharField(choices=[('general', 'General'), ('web', 'Web')], default='general', max_length=16, verbose_name='Type')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('protocols', models.JSONField(default=list, verbose_name='Protocol')),
                ('tags', models.JSONField(default=list, verbose_name='Tags')),
                ('comment', models.TextField(blank=True, default='', verbose_name='Comment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AppletHost',
            fields=[
                ('host_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='assets.host')),
                ('account_automation', models.BooleanField(default=False, verbose_name='Account automation')),
                ('date_synced', models.DateTimeField(blank=True, null=True, verbose_name='Date synced')),
                ('status', models.CharField(max_length=16, verbose_name='Status')),
            ],
            options={
                'abstract': False,
            },
            bases=('assets.host',),
        ),
        migrations.CreateModel(
            name='AppletPublication',
            fields=[
                ('created_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Created by')),
                ('updated_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Updated by')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('status', models.CharField(default='', max_length=16, verbose_name='Status')),
                ('comment', models.TextField(blank=True, default='', verbose_name='Comment')),
                ('applet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='terminal.applet', verbose_name='Applet')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='terminal.applethost', verbose_name='Host')),
            ],
            options={
                'unique_together': {('applet', 'host')},
            },
        ),
        migrations.CreateModel(
            name='AppletHostDeployment',
            fields=[
                ('created_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Created by')),
                ('updated_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Updated by')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=16, default='', verbose_name='Status')),
                ('comment', models.TextField(blank=True, default='', verbose_name='Comment')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='terminal.applethost', verbose_name='Hosting')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='applethost',
            name='applets',
            field=models.ManyToManyField(through='terminal.AppletPublication', to='terminal.Applet', verbose_name='Applet'),
        ),
    ]
