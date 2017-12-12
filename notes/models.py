from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class MatiereModel(models.Model):
    class Meta:
        verbose_name_plural=_('Matière')
        verbose_name=_('Matière')
    nom_matiere = models.CharField(verbose_name=_('Matière'), max_length=255,)
    coefficient = models.DecimalField(verbose_name=_('Coefficient de la matière'), max_digits=4, decimal_places=3, default=1)
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
    #matiere = models.CharField(verbose_name=_('Matière'), max_length=30)
    matiere = models.ForeignKey(MatiereModel, on_delete=models.CASCADE, verbose_name=_('Matière'))
    nom = models.CharField(verbose_name=_('Nom du contrôle'), max_length=255, default='IE')
    desc = models.CharField(verbose_name=_('Description du contrôle'), max_length=255, blank=True)
    date = models.DateTimeField(verbose_name=_('Date du contrôle'))
    note = models.IntegerField(verbose_name=_('Note /20'))
    coef = models.DecimalField(verbose_name=_('Coefficient'), max_digits=4, decimal_places=3, default=1)
    typenote = models.ForeignKey(TypeNote, on_delete=models.CASCADE, verbose_name=_('Type de note'))
    def __str__(self):
        return str(self.nom) + ", " + str(self.note) + "/20"