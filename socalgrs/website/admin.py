# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from website.models import *
from django.contrib import admin



# Register your models here.

class RailwayAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ['title']

admin.site.register(Railway, RailwayAdmin)

class RailwayImageAdmin(admin.ModelAdmin):
    list_display = ('railway', 'position','image')
    search_fields = ['title']

admin.site.register(RailwayImage, RailwayImageAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'position')
    search_fields = ['title']

admin.site.register(Event, EventAdmin)
