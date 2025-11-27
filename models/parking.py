#les models sont les entités principales de notre programme

from .abonnement import Abonnement
from .client import Client

from .place import Place
from .voiture import Voiture

from composants import camera

# un parking a un nom , un prix , un ensemble de places et un nombre de niveaux
class Parking:
    def __init__(self,nom,prix,nbNiveaux):
        self.nom = nom
        self.prix = prix
        self.places = []
        self.nbNiveaux = nbNiveaux
        self.abonnements = {} #permet de stocker les clients abonnés 


    """
    OPERATIONS OBSERVATRICES
    -connaitre le nombres de places par niveau
    -connaitre le nombre de places du parking
    -connaitre le nombre de places libres
    
    OPERATIONS MODIFICATRICES
    -rechercher une place
    -ajouter un abonnement 
    -ajouter une place à un parking
    """

    def nbPlaces(self):
        return len(self.places)
    
    def nbPlacesLibres(self):
        nbLibre = 0
        for p in self.places:
            if p.estLibre:
                nbLibre += 1
        return nbLibre

    def nbPlacesLibresParNiveau(self):
        for niveau in range(self.nbNiveaux):
            nbLibre = 0

            for p in self.places:
                if p.niveau == niveau and p.estLibre:
                    nbLibre += 1

            print("Niveau", niveau, ":" , nbLibre, "places libres")

    
    def ajouterPlace(self,p):
        self.places.append(p)
    
    def ajouterAbonnement(self,client):
        if client.idClient in self.abonnements:
            print(f"Le client {client.nom} est déjà abonné.")
            return False
        abonnement = Abonnement(client)
        self.abonnements[client.idClient] = abonnement
        print(f"abonnement ajouté pour le client n°{client.nom} .")
        

    def rechercherPlace(self,voiture):
        for p in self.places:
            if p.estLibre:
                p.occuperPlace(voiture)
                return p 
        print("aucune place disponible!")
        return None








