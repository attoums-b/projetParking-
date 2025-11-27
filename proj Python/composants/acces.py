import camera, panneau_affichage 
class Acces:
    def actionnerCamera(self, voiture):
        # si il y'a une voiture
        if voiture():
        #j'appelle les methodes que doit faire la camera
            camera.capturerHauteurVoit(voiture)
            camera.capturerLongueurVoit(voiture)
            camera.capturerImmat(voiture)

    def actionnerPanneau(self):
        if voiture():
            panneau_affichage.afficher_instructions()
            panneau_affichage.proposerAbonnement()
    def lancerProcedureEntree(self,client):
        pass