# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(NotesModel)
class BasicAdmin(admin.ModelAdmin):
    pass
