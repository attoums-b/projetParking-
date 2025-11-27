from models import voiture

class Camera:



    # la camera est chargée de récuperer la hauteur de la voiture 
    def capturerHauteurVoit(self,v):
        return v.hauteur

    def capturerLongueurVoit(self,v):
        return v.longueur

    def capturerImmat(self,v):
        return v.immatriculation



    def retournerValeur(self):
        return self.parking.nbPlacesLibres() > 0

#la caméra va garder les informations de la voiture

