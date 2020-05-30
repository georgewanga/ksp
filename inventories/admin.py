from django.contrib import admin
from .models import (
    Units,Categories,Products
)

admin.site.register(Units)
admin.site.register(Categories)
admin.site.register(Products)