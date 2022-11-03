# Generated by Django 3.2.14 on 2022-10-27 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0012_auto_20220816_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='connectiontoken',
            name='protocol',
            field=models.CharField(choices=[('ssh', 'SSH'), ('rdp', 'RDP'), ('telnet', 'Telnet'), ('vnc', 'VNC'), ('mysql', 'MySQL'), ('mariadb', 'MariaDB'), ('oracle', 'Oracle'), ('postgresql', 'PostgreSQL'), ('sqlserver', 'SQLServer'), ('redis', 'Redis'), ('mongodb', 'MongoDB'), ('k8s', 'K8S'), ('http', 'HTTP'), ('None', ' Settings')], default='ssh', max_length=16, verbose_name='Protocol'),
        ),
    ]