class Place:
    compteur = {}   # compteur par niveau

    def __init__(self, niveau, longueur, hauteur, estLibre=True):
        # initialiser compteur pour ce niveau si nécessaire
        if niveau not in Place.compteur:
            Place.compteur[niveau] = 0

        Place.compteur[niveau] += 1

        self.niveau = niveau
        self.numero = Place.compteur[niveau]
        self.idPlace = f"{niveau}{self.numero}"

        self.longueur = longueur
        self.hauteur = hauteur
        self.estLibre = estLibre
        self.voiture = None

    def estOccupe(self):
        return not self.estLibre

    def occuperPlace(self, voiture):
        self.voiture = voiture
        self.estLibre = False

    def libererPlace(self):
        self.voiture = None
        self.estLibre = True
