from camera import Camera
from panneau_affichage import PanneauAffichage

class Acces:
    def actionnerCamera():
        #la camera va executer ces trois fonctions
        Camera.capturerHauteur()
        Camera.capturerLongueur()
        Camera.capturerImmat()

    def actionnerPanneau():
        PanneauAffichage.afficherPlacesDisponibles()
        #le panneau d'affichage va afficher les places disponibles
