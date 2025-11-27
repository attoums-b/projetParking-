class Voiturier:
    def __init__(self, numero):
        self.numero = numero

    def livrer_voiture(self, voiture, adresse):
        print("Voiturier", self.numero, "livre la voiture", voiture.immatriculation, "à", adresse)
