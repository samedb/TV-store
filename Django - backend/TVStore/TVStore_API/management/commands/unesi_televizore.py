from TVStore_API.models import TV
from django.core.management.base import BaseCommand, CommandError
import json
from pprint import pprint

class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Hello")
        with open('televizori.txt', 'r') as infile:
            data = json.load(infile)
        
        for item in data:
            #pprint(item)
            # Razocarao sam se u python sa ovim, nema ni ternarni operator ;(
            tv = TV(
                ean = item['EAN kod'],
                cena = item['cena'],
                dostupno = True,
                proizvodjac = item['proizvodjac'],
                model = item['Model'],
                dijagonala = item['Dijagonala'] if "Dijagonala" in item else 32,
                rezolucija = item['Rezolucija'] if 'Rezolucija' in item else '1366 x 768',
                smart = item['SMART'] if "SMART" in item else 'Ne',
                ekran = item['Ekran'] if 'Ekran' in item else 'LCD',
                tip_tunera = item['Tip Tunera'] if 'Tip Tunera' in item else 'Digitalni',
                energetski_razred = item['Energetski razred'] if 'Energetski razred' in item else 'B',
                wireless = item['Wireless'] if 'Wireless' in item else 'Ne',
                povezivanje = item['Povezivanje'] if 'Povezivanje' in item else '',
                vesa = item['VESA Monta\u017ea'] if 'VESA Monta\u017ea' in item else 'Ne',
                boja = item['Boja'] if 'Boja' in item else 'Crna',
                dvb_c = item['DVB-C'] if 'DVB-C' in item else 'Ne',
                dvb_s2 = item['DVB-S2'] if 'DVB-S2' in item else 'Ne',
                dvb_t2 = item['DVB-C'] if 'DVB-C' in item else 'Ne',
                zvucnici = item['Zvu\u010dnici'] if 'Zvu\u010dnici' in item else '',
                masa = item['Masa'] if 'Masa' in item else '',
                dimenzije = item['Dimenzije']if 'Dimenzije' in item else '',
                dodatne_prednosti = item['Dodatne prednosti'] if 'Dodatne prednosti' in item else '',
                slike = item['slike'] if 'slike' in item else '',
                ostalo = item['Ostalo'] if 'Ostalo' in item else '',
                napomena = item['Napomena'] if 'Napomena' in item else '',
            )
            print(tv.boja)
            tv.save()

        print("Kraj ove komande")