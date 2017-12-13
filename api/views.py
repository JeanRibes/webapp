from rest_framework import viewsets
from api.serializers import NotesSerializer, MatiereSerializer
from notes.models import NotesModel, MatiereModel


# Create your views here.
class NotesViewSet(viewsets.ModelViewSet):
    queryset = NotesModel.objects.all()
    serializer_class = NotesSerializer


class MatiereViewSet(viewsets.ModelViewSet):
    queryset = MatiereModel.objects.all()
    serializer_class = MatiereSerializer
