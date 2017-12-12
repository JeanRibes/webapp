from django.http import HttpResponse
from django.shortcuts import render
from notes.models import NotesModel
# Create your views here.
def moyenne(request):
    Notes = NotesModel.objects.get.all()
#    notes = Notes.note
    somme = 0
    for i in notes:
        somme += notes[i]
    return HttpResponse(somme)



