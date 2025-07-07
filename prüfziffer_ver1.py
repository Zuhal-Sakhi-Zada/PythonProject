# Der Algorithmus berechnet die Prüfziffer einer ISBN-13.
# Dabei wird jede zweite Zhal (beginnend mit der zweiten Ziffer ungerader Index) mit 3 multipliziert.
# Die restlichen Ziffer werden normal addiert und all diese Werte werden anschließend zusammengezählt.
# Die Prüfziffer ist so gewählt, dass die Gesamtsumme (die Summer der Werte + die Prüfziffer) glatt durch 10 teilbar ist.

def isbn13_prüfziffer(isbn12):
    summe=0
    for i in range(12):
        ziffer=int(isbn12[i])
        if i % 2==0:
            summe+=ziffer
        else:
            summe+=3*ziffer
    prüfziffer = (10-(summe%10))%10
    return prüfziffer

isbn = input("Geben Sie die ersten 12 Ziffern der ISBN-13 ein: ")

if len(isbn) != 12 or not isbn.isdigit():
    print("Fehler: Bitte geben Sie genau 12 Ziffern ein.")
else:
    prüfziffer = isbn13_prüfziffer(isbn)
    print(f"Die Prüfziffer lautet: {prüfziffer}")
    print(f"Die vollständige ISBN-13 lautet: {isbn}{prüfziffer}")