from .models import *
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"

class OcenaSerializer(serializers.ModelSerializer):
    korisnik_username = serializers.CharField(source="korisnik", read_only=True)
    class Meta: 
        model = Ocena
        fields = ("ocena", "komentar", "korisnik_username")

class TVSerializer(serializers.ModelSerializer):
    class Meta:
        model = TV
        fields = "__all__"

class NaruceniArtiklSerializer(serializers.ModelSerializer):
    class Meta:
        model = NaruceniArtikl
        fields = '__all__'

class PorudzbinaSerializer(serializers.ModelSerializer):
    naruceniartikl_set = NaruceniArtiklSerializer(read_only=True, many=True)
    class Meta:
        model = Porudzbina
        fields = ("ulica", "broj", "grad", "postanski_broj", "telefon", "datumPorudzbine", "zavrsenaPoruzbina", "nacinPlacanja", "naruceniartikl_set")


