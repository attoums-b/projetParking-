class Voiture:
    def __init__(self, hauteur, longueur, immatriculation):
        self.hauteur = hauteur
        self.longueur = longueur
        self.immatriculation = immatriculation
        self.place = None   # la voiture n'occupe pas encore de place

    def addPlacement(self, place):
        """Associe une place à la voiture."""
        self.place = place
