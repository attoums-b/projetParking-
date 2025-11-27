import acces

class PanneauAffichage:
    def afficherNbPlacesDispo(self,parking):
        if acces.actionnerPanneau():
            print(f"Nombres de places disponibles: {parking.nbPlacesLibres()}")


    def afficher_instructions():
        message = """
Bienvenue au Parking DreamPark !🅿️

1- Prendre un ticket à la borne d'entréé
2 avancer pour que la caméra detecte votre véhicule
3- si une place est disponible , placez vous au niveau indiqué


"""
        print(message)


    def afficher_paiement():
        mess = """
Comment voulez-vous payer?:
              -par carte  💳
              -en espece 💰


 faites votre choix --->(carte/espece)?             


"""
        print(mess)


    def proposerAbonnement():
        abo = """

Voulez vous bénéficier d'un abonnement? voici les services disponibles:
              -Livraison de voiture
              -entretien de voiture
              -maintenance

faites votre choix: (OUI / NON) ?


"""

    







