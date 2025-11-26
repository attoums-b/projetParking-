class Place:
    compteur = 0
    def __init__(self,longueur,hauteur, niveau, estLibre=True):
        Place.compteur += 1
        self.numero = Place.compteur
        self.niveau = niveau
        self.idPlace = f"{self.numero},{self.niveau}"
        self.longueur = longueur
        self.hauteur = hauteur
        self.estLibre = estLibre



        """
        Préoccupation : comment attribuer un idPlace dynamiquement
        en fonction du numero et du niveau ?

        OPERATIONS 
        -Occuper une place du parking
        -liberer une place du parking

        
        """

    def occuperPlace(self,voiture):
        if self.estLibre:
            self.voiture = voiture
            voiture.place = self
            self.estLibre = False
            print(f"la voiture {voiture.immatriculation} est garée sur la place {self.idPlace}")
        else:
            print("cette place est déjà occupée")
            

    def libererPlace(self):
        print(f"la voiture{self.voiture.immatriculation} quitte la place {self.idPlace}")
        self.voiture.place = None
        self.voiture = None
        self.estLibre = True

        

        
    
    
        












