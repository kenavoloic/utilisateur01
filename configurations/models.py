from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

class Service(models.Model):
    nom = models.CharField(max_length=255)
    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

class Site(models.Model):
    nom = models.CharField(max_length=255)
    code_postal = models.CharField(max_length=5, validators=[RegexValidator(r'^\d{5}$', 'Un code postal français contient au moins 5 caractères')])

    def __str__(self):
        return f"{self.nom} ({self.code_postal})"

    class Meta:
        verbose_name = "Site"
        verbose_name_plural = "Sites"

class Conducteur(models.Model):
    erp_id = models.IntegerField(unique=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    date_naissance = models.DateField(null=True, blank=True)
    date_entree = models.DateField()
    date_sortie = models.DateField(null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    actif_p = models.BooleanField(default=True, verbose_name="Actif")
    interim_p = models.BooleanField(default=False, verbose_name="Intérim")

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    @property
    def nom_complet(self):
        return f"{self.prenom} {self.nom}"

    class Meta:
        verbose_name = "Conducteur"
        verbose_name_plural = "Conducteurs"
        ordering = ['nom', 'prenom']        

# class Notateur(models.Model):
#     nom = models.CharField(max_length=255)
#     prenom = models.CharField(max_length=255)
#     date_entree = models.DateField()
#     date_sortie = models.DateField(null=True, blank=True)
#     service = models.ForeignKey(Service, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.prenom} {self.nom}"

#     @property
#     def nom_complet(self):
#         return f"{self.prenom} {self.nom}"

#     class Meta:
#         verbose_name = "Notateur"
#         verbose_name_plural = "Notateurs"

# class CriteresNotation(models.Model):
#     nom = models.CharField(max_length=255)

#     def __str__(self):
#         return self.nom

#     class Meta:
#         verbose_name = "Critère de notation"
#         verbose_name_plural = "Critères de notation"

# class Notation(models.Model):
#     date_notation = models.DateField()
#     notateur = models.ForeignKey(Notateur, on_delete=models.CASCADE)
#     conducteur = models.ForeignKey(Conducteur, on_delete=models.CASCADE)
#     critere = models.ForeignKey(CriteresNotation, on_delete=models.CASCADE)
#     valeur = models.IntegerField(null=True, blank=True)

#     def __str__(self):
#         return f"{self.conducteur} - {self.critere} : {self.valeur}"

#     class Meta:
#         verbose_name = "Notation"
#         verbose_name_plural = "Notations"
#         unique_together = ['conducteur', 'critere', 'date_notation', 'notateur']

# class HistoriqueNotation(models.Model):
#     notation = models.ForeignKey(Notation, on_delete=models.CASCADE)
#     critere = models.ForeignKey(CriteresNotation, on_delete=models.CASCADE)
#     ancienne_valeur = models.IntegerField(null=True, blank=True)
#     nouvelle_valeur = models.IntegerField()
#     date_changement = models.DateTimeField(default=timezone.now)

#     class Meta:
#         verbose_name = "Historique de notation"
#         verbose_name_plural = "Historiques de notation"

# class HistoriqueSite(models.Model):
#     conducteur = models.ForeignKey(Conducteur, on_delete=models.CASCADE)
#     site = models.ForeignKey(Site, on_delete=models.CASCADE)
#     date_entree = models.DateField()
#     date_sortie = models.DateField(null=True, blank=True)

#     class Meta:
#         verbose_name = "Historique de site"
#         verbose_name_plural = "Historiques de site"        
