class  konto:
    def __init__(self, kontonummer, kontoinhaber, kontostand, dispozinssatz):
        self.__kontonummer = kontonummer
        self.kontoinhaber = kontoinhaber
        self.__kontostand = kontostand
        self.__dispozinssatz = dispozinssatz


    def kontonummer(self):
        return self.__kontonummer

    def dispozinssatz(self):
        return self.__dispozinssatz

    passwort= "123456"

    def get_kontostand(self):
        i=3
        while i>0:
            passwort=input("Passwort eingeben: ")
            i-=1
            if passwort == self.passwort:
                print("Zugriff erlaubt")
                return self.__kontostand
            else:
                if i==0:
                    print("Password wurde dreimal falsch eingegeben!")
                    return
                else:
                    print(f"Sie haben noch {i} Versuche")

    def set_kontostand(self, betrag):
        self.__kontostand += betrag

    def einzahlen(self, betrag:float):
        if betrag <= 0:
            print("Betrag muss positiv sein.")
        else:
            self.__kontostand += betrag
            print(f"{betrag}€ eingezahlt")

    def abheben(self, betrag:float):
        if betrag > self.__kontostand:
            print("Geben Sie einen kleineren Betrag an")
        elif betrag <= 0:
            print("Betrag muss positiv sein")
        else:
            self.__kontostand -= betrag
            print(f"{betrag}€ abgehoben")
    def kontostand_anzeigen(self):
        print(f"Aktueller Kontostand: {self.__kontostand:.2f}€")

k1 = konto(233423432, "zuhal", 500, 10)
k1.get_kontostand()
k1.einzahlen(400)
k1.abheben(20)
k1.kontostand_anzeigen()
print(f"Dispozinssatz: {k1.dispozinssatz()}%")
print(f"kontonummer: {k1.kontonummer()}")
