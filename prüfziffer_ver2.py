# Die ISBN-10 besteht aus 9 Ziffern und eine Prüfzahl.
# Beim Berechnen der Prüfziffer werden die ersten neun Ziffer mit ihrer Position(1-9) multipliziert und alle Produkte addiert.
# Die Summe wird schließlich durch 11 geteilt. Falls das Ergebnis 10 ist, wird die Prüfziffer als "X" dargestellt.

def isbn10_prüfziffer(isbn9):
    summe=0
    for i in range(9):
        ziffer=int(isbn9[i])
        summe += (i+1) * ziffer

    prüfziffer = summe % 11

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