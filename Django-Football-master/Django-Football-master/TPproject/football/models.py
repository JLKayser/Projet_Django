from django.db import models

class Club(models.Model): #déclare la classe Livre héritant de la classe Model, classede base des modèles
    nom_club = models.CharField(max_length=100) # défini un champs de type texte de 100 caractères maximum
    pays_club = models.CharField(max_length = 100)
    date_parution_club = models.DateField(blank = True, null = True) # champs de type date,pouvant être null ou ne pas être rempli
    nombre_LDC = models.IntegerField(blank = False) # champs de type entier devant être obligatoirement rempli
    resume = models.TextField(null = True, blank = True) # champs de type text long

    def __str__(self):
        chaine = f"{self.nom_club}"
        return chaine

class Joueur(models.Model):
    nom_joueur = models.CharField(max_length=100)  # défini un champs de type texte de 100 caractères maximum
    pays_joueur = models.CharField(max_length=100)
    date_naissance_joueur = models.DateField(blank=True, null=True)  # champs de type date,pouvant être null ou ne pas être rempli
    nombre_LDC = models.IntegerField(blank=False)  # champs de type entier devant être obligatoirement rempli
    resume = models.TextField(null=True, blank=True)  # champs de type text long
    club = models.ForeignKey(Club, on_delete=models.CASCADE,default= None, null=True)

    def __str__(self):
        chaine = f"{self.nom_joueur} est origine du pays {self.pays_joueur} et le joueur est né en"
        return chaine