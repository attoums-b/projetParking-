class Client:
    # Initialise un client
    def __init__(self, id_client, nom, adresse):
        self.id_client = id_client
        self.nom = nom
        self.adresse = adresse
        self.abonne = False
        self.historique_demandes = []

    # Vérifie si le client est abonné
    def est_abonne(self):
        return self.abonne

    # Abonne le client
    def abonner(self):
        self.abonne = True

    # Désabonne le client
    def desabonner(self):
        self.abonne = False

    # Ajoute une demande de maintenance
    def demander_maintenance(self):
        self.historique_demandes.append("maintenance")

    # Ajoute une demande de livraison
    def demander_livraison(self, date, heure, adresse_livraison):
        self.historique_demandes.append(
            {"type": "livraison", "date": date, "heure": heure, "adresse": adresse_livraison}
        )

    # Ajoute une demande d’entretien
    def demander_entretien(self):
        self.historique_demandes.append("entretien")
