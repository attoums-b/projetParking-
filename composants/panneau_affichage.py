class PanneauAffichage:
    def afficherPlacesDisponibles(self,p):
        #on parcours pour un parking , sa liste de places
        for places in p.places:
            #on vérifie la disponibilité de la place
            if places.estLibre:
                #si c'est le cas , on affiche les places
                print(places)

        
            




    







