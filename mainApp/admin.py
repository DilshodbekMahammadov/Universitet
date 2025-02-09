from django.contrib import admin
from .models import *

class UstozAdmin(admin.ModelAdmin):
    list_display = ['ism', 'daraja']
    search_fields = ['ism']
    search_help_text = 'Ustoz ismini kiriting'

class YonalishAdmin(admin.ModelAdmin):
    list_display = ['nom', 'aktiv']
    list_filter = ['aktiv']
    search_fields = ['nom']

class FanAdmin(admin.ModelAdmin):
    list_filter = ['asosiy', 'yonalish']
    search_fields = ['nom']

admin.site.register(Yonalish, YonalishAdmin)
admin.site.register(Fan, FanAdmin)
admin.site.register(Ustoz, UstozAdmin)
