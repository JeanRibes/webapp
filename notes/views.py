from django.http import HttpResponse
from django.shortcuts import render
from notes.models import NotesModel, MatiereModel

def calculMoyenne(NotesModel, MatiereModel):
    n, sommeNotes, sommeMatiere, nM = 0, 0, 0, 0
    for matiere in MatiereModel.objects.all():  # on parcourt toutes les matières
        sommeMatiere = 0  # nécessaire sinon KeyError
        nM = 0
        for note in NotesModel.objects.filter(matiere=matiere):  # on parcourt toutes les notes d'une matière donnée
            sommeMatiere += note.note * note.coef  # on ajoute la note pondérée du coefficient de la note à la somme de la matière donnée
            nM += note.coef * matiere.coefficient  # on calcule le nombre de "notes virtuelles"
        sommeNotes += sommeMatiere * matiere.coefficient  # on ajoute les sommes de matière, pondérée par le coefficient de la matièr
        n += nM
        return round(sommeNotes/n, 2)
# Create your views here.
def moyenne(request):
    n, sommeNotes , sommeMatiere, nM= 0, 0, 0, 0
    for matiere in MatiereModel.objects.all():  # on parcourt toutes les matières
        sommeMatiere = 0  # nécessaire sinon KeyError
        nM = 0
        for note in NotesModel.objects.filter(matiere=matiere):  # on parcourt toutes les notes d'une matière donnée
            sommeMatiere += note.note * note.coef  # on ajoute la note pondérée du coefficient de la note à la somme de la matière donnée
            nM += note.coef * matiere.coefficient  # on calcule le nombre de "notes virtuelles"
        sommeNotes += sommeMatiere * matiere.coefficient  # on ajoute les sommes de matière, pondérée par le coefficient de la matièr
        n += nM
    return HttpResponse(round(sommeNotes / n, 2))

def listeNotes(request, matiere):
    Matiere = MatiereModel.objects.get(nom_matiere=matiere)
    Notes = NotesModel.objects.filter(matiere=Matiere)
    return render(request, 'listeNotes.html', {'matiere':Matiere,
                                               'Notes':Notes,
                                               'newId': NotesModel.objects.latest(field_name='id').id + 1})

def listeMatieres(request):
 #   Matieres = dict(MatiereModel.objects.all())
 #   for matiere in Matieres:
 #       Matieres['moyenne'] = matiere.moyenne()
    Matieres = {}
    for matiere in MatiereModel.objects.all():
        Matieres[matiere.nom_matiere] = {'nom_matiere':matiere.nom_matiere,
                         'coefficient': matiere.coefficient,
                         'moyenne': matiere.moyenne,
                         }
   # for matiere in MatiereModel.objects.all():
   #
   #     Matieres['nom_matiere'] = matiere.nom_matiere
   #     Matieres['coefficient'] = matiere.coefficient
   #     Matieres['moyenne'] = matiere.moyenne()
    render(request, template_name='listeMatieres.html', context=Matieres)
    return render(request, 'listeMatieres.html', context={'Matieres':Matieres, 'moyenneGenerale': calculMoyenne(NotesModel=NotesModel, MatiereModel=MatiereModel),
                                                          'newId': NotesModel.objects.latest(field_name='id').id+1})
