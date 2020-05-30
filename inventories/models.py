from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from autoslug import AutoSlugField

import datetime


class Units(models.Model):
    name = models.CharField(
        max_length=32,
    )

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(
        max_length=32,
    )

    def __str__(self):
        return self.name


class Products(models.Model):
    key = models.CharField(
        max_length=8,
    )
    image = models.ImageField(
        blank=True,
    )
    name = models.CharField(
        max_length=32,
    )
    unit = models.ForeignKey(
        Units,
        on_delete=models.DO_NOTHING,
    )
    category = models.ForeignKey(
        Categories,
        on_delete=models.DO_NOTHING,
    )
    q = models.PositiveSmallIntegerField(
        verbose_name=_('Quantity'),
    )
    q_reserve = models.PositiveSmallIntegerField(
        verbose_name=_('Quantity Reserve'),
        help_text=_(
            'Is the minimum quantity of the product that indicates that you must buy more product.'
        ),
    )
    pur_price = models.DecimalField(
        verbose_name=_('Purchase Price'),
        decimal_places=2,
        max_digits=19,
        default=0,
    )
    sal_price = models.DecimalField(
        verbose_name=_('Sale Price'),
        decimal_places=2,
        max_digits=19,
        default=0,
    )
    info = models.TextField(
        verbose_name=_('Additional Product Information.'),
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
        return reverse("inventories:detail", args=[str(self.slug)])

    def __str__(self):
        return self.name
