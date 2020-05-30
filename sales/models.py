from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from autoslug import AutoSlugField

from inventories.models import Products
from services.models import Services

import datetime


class PaymentMethods(models.Model):
    name = models.CharField(
        max_length=32,
    )

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(
        max_length=32,
    )

    def __str__(self):
        return self.name


class Sales(models.Model):
    product = models.ForeignKey(
        'inventories.Products',
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    service = models.ForeignKey(
        'services.Services',
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    q = models.PositiveSmallIntegerField(
        verbose_name=_('Quantity'),
    )
    sale = models.DecimalField(
        verbose_name=_('Sale KSh'),
        decimal_places=2,
        max_digits=19,
        default=0,
    )
    subtotal = models.DecimalField(
        verbose_name=_('Subtotal KSh'),
        decimal_places=2,
        max_digits=19,
        default=0,
    )
    paid = models.BooleanField(
        verbose_name=_('Paid?'),
        default=True,
        help_text=_('Paid, unchecked if receivables')
    )
    client = models.CharField(
        verbose_name=_('Client Name'),
        max_length=128,
        blank=True,
        null=True,
    )
    p_method = models.ForeignKey(
        PaymentMethods,
        on_delete=models.DO_NOTHING,
        verbose_name=_('Payment Method'),
        blank=True,
        null=True,
    )
    tag = models.ForeignKey(
        Tags,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    info = models.TextField(
        verbose_name=_('Additional Information.'),
        null=True,
        blank=True,
    )
    pub_date = models.DateTimeField(
        verbose_name=_('Date Added'),
        auto_now=True
    )
    slug = AutoSlugField(populate_from='name', unique_with='pub_date__month')

    def was_added_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def get_absolute_url(self):
        return reverse("sales:detail", args=[str(self.slug)])

    def __str__(self):
        return self.name
