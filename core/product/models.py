from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from core.models import BaseModel
from core.store.models import Store


class Product(BaseModel):
    name = models.CharField(max_length=255, db_column='name', verbose_name=_('Name'))

    price = models.PositiveIntegerField(validators=[MinValueValidator(1)], db_column='price', blank=True, verbose_name=_('Price'))

    store = models.ForeignKey(Store, on_delete=models.RESTRICT, related_name='product')

    class Meta:
        db_table = 'product'
        verbose_name_plural = _('Product')
