from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from autoslug import AutoSlugField
import datetime


class Services(models.Model):
    name = models.CharField(
        verbose_name=_('Service Name'),
        max_length=32,
    )
    inv_cost = models.DecimalField(
        verbose_name=_('Cost Investment'),
        decimal_places=2,
        max_digits=19,
        default=0,
        help_text=_('The investment cost refers to the money invested to perform the service (this information is used to obtain profit). Theinvestment cost can be zero.'),
    )
    sal_price = models.DecimalField(
        verbose_name=_('Sale Price'),
        decimal_places=2,
        max_digits=19,
        default=0,
    )
    info = models.TextField(
        verbose_name=_('Additional Service Information.'),
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
        return reverse("services:detail", args=[str(self.slug)])

    def __str__(self):
        return self.name
