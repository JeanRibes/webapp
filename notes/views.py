from django.http import HttpResponse
from django.shortcuts import render
from notes.models import NotesModel, MatiereModel


# Create your views here.
def moyenne(request):
    n, sommeNotes = 0, 0
    sommeMatiere = {}

    for matiere in MatiereModel.objects.all():  # on parcourt toutes les matières
        sommeMatiere[matiere.id] = 0  # nécessaire sinon KeyError
        for note in NotesModel.objects.filter(matiere=matiere):  # on parcourt toutes les notes d'une matière donnée
            sommeMatiere[matiere.id] += note.note * note.coef  # on ajoute la note pondérée du coefficient de la note à la somme de la matière donnée
            n += note.coef * matiere.coefficient  # on calcule le nombre de "notes virtuelles"
        sommeNotes += sommeMatiere[
                          matiere.id] * matiere.coefficient  # on ajoute les sommes de matière, pondérée par le coefficient de la matière

    return HttpResponse(round(sommeNotes / n, 2))

def listeNotes(request, matiere):
    Matiere = MatiereModel.objects.filter(nom_matiere=matiere)
    return HttpResponse(Matiere.nom_matiere)
    id_matiere = Matiere.nom_matiere
    Notes = NotesModel.objects.filter(matiere=id_matiere)
    return render(request, 'listeNotes.html', {'matiere':matiere,
                                               'Notes':Notes})
