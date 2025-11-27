class Abonnement:
    # Initialise l'abonnement
    def __init__(self, libelle, prix, estPackGar):
        self.libelle = libelle
        self.prix = prix
        self.estPackGar = estPackGar
        self.contrats = []

    # Ajoute un contrat à l'abonnement
    def ajouter_contrat(self, contrat):
        self.contrats.append(contrat)
