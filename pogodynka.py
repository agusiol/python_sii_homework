"""
Napisz program pogodynka

Po podaniu przez uzytkownika dnia i miesiaca zaproponuj pogodę na ten dzien.
Uwzglednij:
- pore roku (np. jesienią jest zwykle deszczowo)
- temperature (przedstawiona w sopniach Farhenheita, Celcjusza i w Kelvinach)

Dla chetnych:
- uwzglednij opady
- uwzglednij stopien zachmurzenia / naslonecznienia
- uwzglednij kierunek i sile wiatru

Z gwiazdka :) - pokus sie o pobranie roku od uzytkownika i dodaj zabawny komentarz

Podpowiedzi:
Uzyj instrukcji warunkowych if/elif/else
Jesli robisz zadania dla chetnych skorzystaj z modulu random
"""
import random

months = {
    "Styczeń": 31,
    "Luty": 29,
    "Marzec": 31,
    "Kwiecień": 30,
    "Maj": 31,
    "Czerwiec": 30,
    "Lipiec": 31,
    "Sierpień": 31,
    "Wrzesień": 30,
    "Pzdziernik": 31,
    "Listopad": 30,
    "Grudzień": 31,
}

# Asking for user input
while month := input("Podaj miesiac").title():
    if month not in months:
        print("Podaj poprawny")
    else:
        break

while day := int(input("Podaj dzień")):
    max_days = months[month]
    if max_days < day < 1:
        print("Zly dzien")
    else:
        break

#SEASON DESCRIPTION
seasons = {
    "Zima": {
        "months": ["Styczeń", "Luty", "Marzec"],
        "temp_range": [-30, 10],
    },
    "Wiosna": {
        "months": ["Kwiecień", "Maj", "Czerwiec"],
        "temp_range": [5, 25],
    },
    "Lato": {
        "months": ["Lipiec", "Sierpień", "Wrzesień"],
        "temp_range": [15, 35],
    },
    "Jesień": {
        "months": ["Październik", "Listopad", "Grudzień"],
        "temp_range": [0, 15],
    },
}

#GET THE SEASON
for s in seasons:
    if month in seasons[s]["months"]:
        season = s

if month == "Marzec" and day >= 21:
    season = "Wiosna"
elif month == "Czerwiec" and day >= 22:
    season = "Lato"
elif month == "Wrzesień" and day >= 23:
    season = "Jesień"
elif month == "Grudzień" and day >= 24:
    season = "Zima"

#GET THE TEMPERATURE
temp_min = seasons[season]["temp_range"][0]
temp_max = seasons[season]["temp_range"][1]

temp_C = random.randrange(temp_min,temp_max)
temp_K = round(temp_C + 273.15)
temp_F = round(temp_C * 9/5 +32)

degree = u"\u00b0"

# CLOUDY/SUNNY
sky = ['pochmurno', 'częściowo pochmurono', 'częściowo słonecznie', 'słonecznie']
weather = random.choice(sky)

#PRECIPITATION
if weather != 'słonecznie':
    rain = random.choice([True,False])
else:
    rain = False

print(f"Jest {season}!")
print(f"Dzisiaj jest {weather} i {'nie ' if not rain else ''}pada {'deszcz' if temp_C >= 0 else 'śnieg'}.")
print(f"Temperatura wynosi {temp_C}{degree}C/{temp_F}{degree}F/{temp_K}K")