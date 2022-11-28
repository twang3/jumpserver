import os.path
import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.db.models import BaseCreateUpdateModel


class Playbook(BaseCreateUpdateModel):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=128, verbose_name=_('Name'), null=True)
    path = models.FileField(upload_to='playbooks/')
    owner = models.ForeignKey('users.User', verbose_name=_("Owner"), on_delete=models.SET_NULL, null=True)

    @property
    def work_path(self):
        return os.path.join(settings.DATA_DIR, "ops", "playbook", self.id.__str__(), "main.yaml")