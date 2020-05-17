from .models import *
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"

class OcenaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Ocena
        fields = "__all__"

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


