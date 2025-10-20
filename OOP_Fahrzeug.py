class fahrzeug:
    def __init__(self, strecke, zeit, Anfangsgeschwindigkeit):
        #Eigenschaften
        self.s = strecke
        self.t = zeit
        self.v0 = Anfangsgeschwindigkeit


    # Methoden
    def geschwindigkeit_berechnen(self):
        self.v = self.s / self.t
        print(f"Geschwindigkeit: {self.v:.2f} m/s")
        return self.v #warum zweimal ausgeben?

    def beschleunigung_berechnen(self):
        self.a = (self.v - self.v0) / self.t
        print(f"Beschleunigung: {self.a:.2f} m/s²")
        return self.a

    def bremsweg_berechnen(self):
        self.bremsweg = self.v**2/(2*self.a)
        print(f"Bremsweg: {self.bremsweg:.2f} m")
        return self.bremsweg


    # Methode Destruktor
    def __del__(self):
        print("Fahrzeug gelöscht!")

# Objekte erzeugen (instanziieren)
fahrzeug1= fahrzeug(20, 30, 0)

fahrzeug1.geschwindigkeit_berechnen()
fahrzeug1.beschleunigung_berechnen()
fahrzeug1.bremsweg_berechnen()
