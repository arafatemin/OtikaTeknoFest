from django.contrib import admin

from .models import *

class InfoOtikaAdmin(admin.ModelAdmin):
    list_display = ('name',  'time', 'durdur', 'bitki_resim', 'x_ekseni', 'y_ekseni')
    list_display_links = ('name',)
    list_editable = ('durdur',)
admin.site.register(InfoOtika, InfoOtikaAdmin)
