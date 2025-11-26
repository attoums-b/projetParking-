from models.voiture import Voiture
from models.client import Client

class BorneTicket:
    def __init__(self,numero):
        self.numero = numero








    def delivrerTicket(self,voiture):
        if voiture.place is not None:
            place = voiture.place
            print(f"""
infos client : 
                  nom: 
                  prenom:
                  prix:
                  place attribuée: {place.idPlace}
""")
            
    def proposerServices(self):
        """
        Bienvenue au parking dreamPark!
        Parking bien aménagé dans lequel vous pouvez trouver des places!!
        Vous pouvez aussi bénéficier d'un abonnement vous offrant des services
        spéciaux [entretien | Livraison | Service]


        
        
        """

    def proposerAbonnement(self,client):
        if client.estAbonne():
            print("Bienvenue! cher abonné")
            return 

        """
        Voulez vous:
            -etre Abonné ?
            -être SuperAbonné ?
        
        """

    def proposerTypePaiment(self):
        """
        Comment Voulez-vous payer?:
        -Par carte bancaire
        -En espèces 

        
        """


    def recupererInfosCarte(self, c):
        pass



            


        

