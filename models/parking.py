#les models sont les entités principales de notre programme


from composants import camera

# un parking a un nom , un prix , un ensemble de places et un nombre de niveaux
class Parking:
    def __init__(self,nom,prix,nbNiveaux):
        self.nom = nom
        self.prix = prix
        self.places = []
        self.nbNiveaux = nbNiveaux


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

    def nbPlacesParNiveau(self):
        pass

    def nbPlaces(self):
        return len(self.places)
    
    def nbPlacesLibres(self):
        nbLibre = 0
        for p in self.places:
            if p.estLibre:
                nbLibre += 1
        return nbLibre
    
    def ajouterPlace(self,p):
        self.places.append(p)
    
    def ajouterAbonnement(self):
        pass

    def rechercherPlace(self,voit):
        """
        idée : parcourir la liste de places
        -si la place est libre:
            retourner immédiatement la premiere place disponible
        -sinon
            afficher: pas de places dispo: désolé mon gars

        """







