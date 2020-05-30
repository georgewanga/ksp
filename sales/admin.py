from django.contrib import admin
from .models import Sales, PaymentMethods, Tags


admin.site.register(PaymentMethods)
admin.site.register(Tags)
admin.site.register(Sales)
