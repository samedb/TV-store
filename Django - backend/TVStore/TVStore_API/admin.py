from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

UserAdmin.fieldsets += ('Custom fields set', {'fields': ('tip', 'naziv_firme', 'pib', 'maticni_broj_firme', 'ulica', 'broj', 'grad', 'postanski_broj', 'telefon')}),


class TVAdmin(admin.ModelAdmin):
    list_display = ('ean', 'proizvodjac', 'model', 'cena', 'cena_na_popustu')

admin.site.register(CustomUser, UserAdmin)
admin.site.register(TV, TVAdmin)
admin.site.register(Ocena)
admin.site.register(Porudzbina)
admin.site.register(NaruceniArtikl)
