# Beim Berechnen der Prüfziffer werden die ersten neun Ziffer mit einer Zahl in absteigender Reihenfolge von 10 bis 2
# multipliziert und diese Werte werden dann addiert. Die Summe wird durch 11 geteilt und der Rest von 11 subtrahiert:
# Falls das Ergebnis 10 ist, wird die Prüfziffer als "X" dargestellt.

def isbn10_prüfziffer(isbn9):
    summe=0
    for i in range(9):
        ziffer=int(isbn9[i])
        multiplikator = 10-i
        summe += ziffer * multiplikator

    prüfziffer = (11-(summe%11))%11

    if prüfziffer == 10:
        return "X"
    else:
        return str(prüfziffer)


isbn = input("Geben Sie die ersten 9 Ziffern der ISBN-10 ein: ")

if len(isbn) != 9 or not isbn.isdigit():
    print("Fehler: Bitte geben Sie genau 9 Ziffern ein.")
else:
    prüfziffer = isbn10_prüfziffer(isbn)
    print(f"Die Prüfziffer lautet: {prüfziffer}")
    print(f"Die vollständige ISBN-10 lautet: {isbn}{prüfziffer}")