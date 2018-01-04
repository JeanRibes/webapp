from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class UEmodel(models.Model):
    class Meta:
        verbose_name = _('Unité d\'enseignement')

    def __str__(self):
        return "#"+str(self.id)+  self.nom_ue + ", coef. " + str(self.coef_ue) + ", moy: " + str(self.moyenneUE)

    # id = models.AutoField(primary_key=True)  C'EST AUTOMATIQUEMENT RAJOUTÉ
    nom_ue = models.CharField(max_length=255, verbose_name=_('Nom'))
    coef_ue = models.DecimalField(verbose_name=_('Coefficient de l\'UE'), max_digits=4, decimal_places=2, default=01.00)
    desc = models.TextField(verbose_name=_('Description de l\'UE'))

    @property
    def moyenneUE(self):
        ecs = list(ECmodel.objects.filter(UE=self))
        somme, n = 0, 0
        for ec in ecs:
            somme += ec.moyenneEC
            n += 1
        if (n > 0):
            moyenne = somme / n
        else:
            moyenne = 10

        return moyenne


class ECmodel(models.Model):
    class Meta:
        verbose_name = _('Élément constutif')

    def __str__(self):
        return "#"+ str(self.id) +' '+ self.nom_ec +", coef."+ str(self.coef_ec) +", moy: "+ str(self.moyenneEC)

    nom_ec = models.CharField(verbose_name=_('Nom'), max_length=255)
    coef_ec = models.DecimalField(verbose_name=_('Coefficient de l\'E.C.'), max_digits=4, decimal_places=2, default=1)
    desc = models.TextField(verbose_name=_('Description de l\'E.C.'))
    UE = models.ForeignKey(UEmodel, on_delete=models.CASCADE)  # pareil, passer à SET_NULL ou autre

    @property
    def moyenneEC(self):
        interros = list(IEmodel.objects.filter(EC=self))
        somme, n = 0, 0
        for interro in interros:
            somme += interro.note
            n += 1
        if (n > 0):
            moyenne = somme / n
        else:
            moyenne = 10
        return moyenne


class IEmodel(models.Model):
    class Meta:
        verbose_name = _('Résultat d\'un contrôle')

    nom_ie = models.CharField(verbose_name=_('Nom du contrôle'), max_length=255, default=_('IE'))
    note = models.DecimalField(max_digits=4, decimal_places=2, default=10)
    coef_ie = models.DecimalField(max_digits=4, decimal_places=2, default=1)
    EC = models.ForeignKey(ECmodel,
                           on_delete=models.CASCADE)  # faudrait mettre SET à la place de CASCADE, pour éviter de perdre des notes si on supprime une EC

    def __str__(self):
        return "#" + str(self.id) + self.nom_ie + ", " + str(self.note) + "/20"
