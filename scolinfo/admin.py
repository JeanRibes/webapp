from django.contrib import admin
from .models import *
# Register your models here.
# -*- coding: utf-8 -*-

@admin.register(UEmodel, ECmodel, IEmodel)
class BasicAdmin(admin.ModelAdmin):
    pass
