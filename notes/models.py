#-*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class MatiereModel(models.Model):
    class Meta:
        verbose_name_plural=_('Matière')
        verbose_name=_('Matière')
    id = models.IntegerField(verbose_name=_('ID'), primary_key=True)
    nom_matiere = models.CharField(verbose_name=_('Matière'), max_length=255,)
    coefficient = models.DecimalField(verbose_name=_('Coefficient de la matière'), max_digits=4, decimal_places=3, default=1)
    #moyenne = models.DecimalField(verbose_name=_('Moyenne dans la matière'), max_digits=4, decimal_places=3, default=0) inutilisé
    def moyenne(self):
        notes = list(NotesModel.objects.filter(matiere=self))
        somme, n = 0, 0
        for note in notes:
            somme+=note.note
            n+=1
        if n>0: return somme/n
        else : return 10
    def __str__(self):
        return str(self.nom_matiere) + ', coef. ' + str(self.coefficient)

class TypeNote(models.Model):
    class Meta:
        verbose_name_plural = _('type de note')
        verbose_name = _('type')
    typeNote = models.CharField(verbose_name=_('Type de note'), max_length=20)
    def __str__(self):
        return str(self.typeNote)

class NotesModel(models.Model):
    class Meta:
        verbose_name_plural = _('notes')
        verbose_name = _('note')
    matiere = models.ForeignKey(MatiereModel, on_delete=models.CASCADE, verbose_name=_('Matière'))
    nom = models.CharField(verbose_name=_('Nom du contrôle'), max_length=255, default='IE')
    desc = models.CharField(verbose_name=_('Description du contrôle'), max_length=255, blank=True)
    date = models.DateField(verbose_name=_('Date du contrôle'))
    note = models.DecimalField(verbose_name=_('Note /20'), max_digits=4, decimal_places=2, default=10.00)
    coef = models.DecimalField(verbose_name=_('Coefficient'), max_digits=4, decimal_places=3, default=1)
    typenote = models.ForeignKey(TypeNote, on_delete=models.CASCADE, verbose_name=_('Type de note'))
    id = models.IntegerField(verbose_name=_('ID'), primary_key=True)
    def __str__(self):
        return str(self.nom) + ", " + str(self.note) + "/20"