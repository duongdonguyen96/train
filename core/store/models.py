from core.models import BaseModel
from django.db import models

from django.utils.translation import ugettext_lazy as _


class Store(BaseModel):
    name = models.CharField(
        max_length=255, db_column='name', blank=True, verbose_name=_('Name'))

    address = models.CharField(
        max_length=255, db_column='address', blank=True, verbose_name=_('Address'))

    class Meta:
        db_table = 'store'
        verbose_name_plural = _('Store')
