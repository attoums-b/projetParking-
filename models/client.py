class client:
    #ajout de id client pour facilités les opération liées à un client
    def __init__(self,idClient,nom,adresse):
        self.idClient = idClient
        self.nom = nom
        self.adresse = adresse
    
    #opération sur les clients
    #nouveau : savoir si un client est abonné --> retourne booléen
    def estAbonne(self):
        pass

    def abonnerClient(self):
        pass

    def desabonnerClient(self):
        pass

    def demanderMaintenance(self):
        pass

    def demanderLivraison(self,date,heure,adresseLiv):
        pass

    def demanderEntretien(self):
        pass