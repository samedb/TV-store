from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from .models import *
from .serializers import *
from django.http import JsonResponse


class UserDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        # print(request.data)
        # Polja koja moze da menja preko PUT
        dozvoljena_polja = ("first_name", "last_name", "email", "tip", "naziv_firme", "pib", "maticni_broj_firme", "ulica", "broj", "grad", "postanski_broj", "telefon")
        for key in request.data:
            if key in dozvoljena_polja:
                setattr(request.user, key, request.data[key])
        request.user.save()

        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)

class TVViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TV.objects.all()
    serializer_class = TVSerializer

class OcenaView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Upisuje ocenu u bazu
    def post(self, request):
        ocena = Ocena(
            ocena = request.data['ocena'],
            komentar = request.data['komentar'] if 'komentar' in request.data else '',
            ean = TV.objects.get(pk=request.data['ean']),
            korisnik = request.user
        )
        ocena.save()
        return Response("Uspesno zapamceno")

    # vraca ocene za neki televizor
    def get(self, request, ean):
        ocene = Ocena.objects.filter(ean=ean)
        serializer = OcenaSerializer(ocene, many=True)
        return Response(serializer.data)

class PorudzbineView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # Uzmi sve moje poruzbine
    def get(self, request):
        porudzbine = Porudzbina.objects.filter(korisnik=request.user)
        serializer = PorudzbinaSerializer(porudzbine, many=True)
        return Response(serializer.data)

    # Dodaj novu porudzbinu
    def post(self, request):
        # Izracunaj sumu svih artikala i uzmi u obzir popust
        ukupna_cena = 0
        for artikl in request.data['artikli']:
            naruceni_tv = TV.objects.get(pk=artikl['ean'])
            if naruceni_tv.cena_na_popustu == 0:
                ukupna_cena += naruceni_tv.cena
            else:
                ukupna_cena += naruceni_tv.cena_na_popustu

        # Kreiraj novu poruzbinu i zapamti je u bazi
        p = Porudzbina(
            ulica=request.data['ulica'],
            broj=request.data['broj'],
            grad=request.data['grad'],
            postanski_broj=request.data['postanski_broj'],
            telefon=request.data['telefon'],
            datumPorudzbine=request.data['datumPorudzbine'],
            nacinPlacanja=request.data['nacinPlacanja'],
            korisnik=request.user,
            ukupna_cena=ukupna_cena,
        )
        p.save()  

        # Zapamti sve artikle u bazi
        for artikl in request.data['artikli']:
            naruceni_tv = TV.objects.get(pk=artikl['ean'])
            cena_koju_racunamo = 0
            if naruceni_tv.cena_na_popustu == 0:
                cena_koju_racunamo = naruceni_tv.cena
            else:
                cena_koju_racunamo = naruceni_tv.cena_na_popustu
            a = NaruceniArtikl(
                id_porudzbine=p,
                ean=naruceni_tv,
                kolicina=artikl['kolicina'],
                cena=cena_koju_racunamo
            )
            a.save()
        return Response("Uspesno unesena porudzbina!")