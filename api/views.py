from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, detail_route
from rest_framework.views import APIView
from notes import models

# Create your views here.
class vue(APIView):
    def voir(request):
        return HttpResponse(models.NotesModel)


class NotesViewSet(APIView):
    #@detail_route(methods='get')
    def list(request):
        notes = models.NotesModel.objects.all()
        return HttpResponse(notes)
    pass