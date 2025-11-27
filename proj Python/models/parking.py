class Parking:
    # Initialise le parking
    def __init__(self, nb_niveaux, prix):
        self.places = []
        self.niveaux = ['A', 'B', 'C', 'D', 'E']
        self.nb_niveaux = nb_niveaux
        self.prix = prix
        # camera à importer ici si besoin

    # Ajoute une place dans le parking
    def ajouter_place(self, place):
        self.places.append(place)

    # Nombre total de places
    def nb_places(self):
        return len(self.places)

    # Nombre de places libres
    def nb_places_libres(self):
        libres = 0
        for place in self.places:
            if place.est_libre:
                libres += 1
        return libres

    # Recherche une place libre
    def rechercher_place(self):
        for place in self.places:
            if place.est_libre:
                return place
        return None

    # Attribue une place à une voiture
    def attribuer_place_voiture(self, voiture):
        place_libre = self.rechercher_place()
        if place_libre is not None:
            place_libre.occuper_place(voiture)
            voiture.place = place_libre
        else:
            print("Aucune place disponible.")

    def retirer_place_voiture(self, voiture):
        if voiture.place is not None:
            voiture.place.liberer_place()
            voiture.place = None
