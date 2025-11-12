class Place:
    def __init__(self,longueur,hauteur, estLibre=True):
        self.numero += 1
        self.niveau = ['A','B','C','D','E']
        self.idPlace = f"{self.numero},{self.niveau}"
        self.longueur = longueur
        self.hauteur = hauteur
        self.estLibre = estLibre

        """
        Préoccupation : comment attribuer un idPlace dynamiquement
        en fonction du numero et du niveau ?

        OPERATIONS 
        -ajouterPlace 
        """










