from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class NotesModel(models.Model):
    class Meta:
        verbose_name_plural = _('notes')
    matiere = models.CharField(verbose_name=_('Matiere'), max_length=30)
    nom = models.CharField(verbose_name=_('nom du controle'), max_length=255)
    desc = models.CharField(verbose_name=_('description du controle'), max_length=255)
    note = models.IntegerField(verbose_name=_('Note /20'))
    coef = models.DecimalField(verbose_name=_('coefficient'), max_digits=4, decimal_places=3, blank=True)
