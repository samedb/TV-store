from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    tip = models.CharField(max_length=20)  # pravno ili fizicko lice
    naziv_firme = models.CharField(max_length=100)
    pib = models.CharField(max_length=20)
    maticni_broj_firme = models.CharField(max_length=20)
    ulica = models.CharField(max_length=50)
    broj = models.CharField(max_length=10)
    grad = models.CharField(max_length=50)
    postanski_broj = models.CharField(max_length=10)
    telefon = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class TV(models.Model):
    ean = models.CharField(max_length=20, primary_key=True)
    cena = models.IntegerField(default=0)
    cena_na_popustu = models.IntegerField(default=0)
    dostupno = models.BooleanField(default=True)
    proizvodjac = models.CharField(max_length=63)
    model = models.CharField(max_length=127)
    dijagonala = models.IntegerField()
    rezolucija = models.CharField(max_length=255, blank=True)
    smart = models.CharField(max_length=127, blank=True)
    ekran = models.CharField(max_length=127, blank=True)
    tip_tunera = models.CharField(max_length=127, blank=True)
    energetski_razred = models.CharField(max_length=31, blank=True)
    wireless = models.CharField(max_length=127, blank=True)
    povezivanje = models.CharField(max_length=500, blank=True)
    vesa = models.CharField(max_length=127, blank=True)
    boja = models.CharField(max_length=127, blank=True)
    dvb_c = models.CharField(max_length=5, default="Ne", blank=True)
    dvb_s2 = models.CharField(max_length=5, default="Ne", blank=True)
    dvb_t2 = models.CharField(max_length=5, default="Ne", blank=True)
    zvucnici = models.CharField(max_length=127, blank=True)
    masa = models.CharField(max_length=127, blank=True)
    dimenzije = models.CharField(max_length=200, blank=True)
    dodatne_prednosti = models.CharField(max_length=500, blank=True)
    slike = models.CharField(max_length=1000, blank=True)
    ostalo = models.CharField(max_length=500, null=True, blank=True)
    napomena = models.CharField(max_length=500, null=True, blank=True)
    
    def __str__(self):
            return f"TV {self.proizvodjac} {self.model} {self.dijagonala}\""

class Ocena(models.Model):
    ocena = models.IntegerField()
    komentar = models.CharField(max_length=500, blank=True)
    korisnik = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    ean = models.ForeignKey(TV, on_delete=models.CASCADE)

    def __str__(self):
        return f"Ocena {self.ocena}"

class Porudzbina(models.Model):
    korisnik = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tip = models.CharField(max_length=20, default="fizicko")  # pravno ili fizicko lice
    naziv_firme = models.CharField(max_length=100, default="")
    pib = models.CharField(max_length=20, default="")
    maticni_broj_firme = models.CharField(max_length=20, default="")
    ulica = models.CharField(max_length=50)
    broj = models.CharField(max_length=10)
    grad = models.CharField(max_length=50)
    postanski_broj = models.CharField(max_length=10)
    telefon = models.CharField(max_length=20)
    datumPorudzbine = models.CharField(max_length=20)
    zavrsenaPoruzbina = models.BooleanField(default=False)
    nacinPlacanja = models.CharField(max_length=50)
    ukupna_cena = models.IntegerField()

class NaruceniArtikl(models.Model):
    id_porudzbine = models.ForeignKey(Porudzbina, on_delete=models.CASCADE)
    ean = models.ForeignKey(TV, on_delete=models.CASCADE)
    cena = models.IntegerField() # cena u trenutku narucivanja
    kolicina = models.IntegerField(default=0)
