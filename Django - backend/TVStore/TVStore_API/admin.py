from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

UserAdmin.fieldsets += ('Custom fields set', {'fields': ('tip', 'naziv_firme', 'pib', 'maticni_broj_firme', 'ulica', 'broj', 'grad', 'postanski_broj', 'telefon')}),


class TVAdmin(admin.ModelAdmin):
    list_display = ('ean', 'proizvodjac', 'model', 'cena', 'cena_na_popustu', 'dostupno')
    list_filter = ('proizvodjac',)
    search_fields = ('ean', 'proizvodjac', 'model',)

class OcenaAdmin(admin.ModelAdmin):
    list_display = ('ean', 'ocena', 'komentar', 'korisnik',)
    list_filter = ('ean',)
    search_fields = ('ean', 'ocena', 'korisnik',)

class NaruceniArtiklInline(admin.TabularInline):
    model = NaruceniArtikl

class PorudzbinaAdmin(admin.ModelAdmin):
    list_display = ('id', 'korisnik', 'datumPorudzbine', 'zavrsenaPoruzbina', 'nacinPlacanja', 'ukupna_cena',)
    list_filter = ('zavrsenaPoruzbina', 'nacinPlacanja')
    search_fields = ('id', 'korisnik',)
    inlines = [
        NaruceniArtiklInline,
    ]


admin.site.register(CustomUser, UserAdmin)
admin.site.register(TV, TVAdmin)
admin.site.register(Ocena, OcenaAdmin)
admin.site.register(Porudzbina, PorudzbinaAdmin)


# class NaruceniArtiklAdmin(admin.ModelAdmin):
#     list_display = ('ean', 'id_porudzbine', 'cena', 'kolicina',)
#     search_fields = ('ean', 'id_porudzbine',)
# admin.site.register(NaruceniArtikl, NaruceniArtiklAdmin)
