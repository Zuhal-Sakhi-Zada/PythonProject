
# Finde den höchsten Aktienkurs der Woche und den höchsten Umsatz pro Tag


import random

aktienkurse = [round(random.uniform(100,200),2) for _ in range(7)]
tage = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]

max_kurs = max(aktienkurse)
max_index = aktienkurse.index(max_kurs)
max_tag = tage[max_index]

print("\nAktienkurse der Woche:")
for tag, kurs in zip(tage, aktienkurse):
    print(f"{tag}: {kurs}€")

print(f"\nHöchster Kurs: {max_kurs}€ am {max_tag}")



import random

umsätze = [random.randint(5000, 15000) for _ in range(7)]
tage = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]


max_umsatz = max(umsätze)
max_index = umsätze.index(max_umsatz)
max_tag = tage[max_index]

# Ausgabe
print("\nUmsätze pro Tag (in €):")
for tag, umsatz in zip(tage, umsätze):
    print(f"{tag}: {umsatz:,} €")

print(f"\nHöchster Umsatz: {max_umsatz:,} € am {max_tag}")
