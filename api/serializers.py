from rest_framework import serializers
from django.contrib.auth.models import User
from notes.models import NotesModel, MatiereModel

class MatiereSerializer(serializers.ModelSerializer):
    moyenne = serializers.ReadOnlyField()
    class Meta:
        model = MatiereModel
        fields = '__all__'
        depth = 2
class NotesSerializer(serializers.ModelSerializer):
    type = serializers.ReadOnlyField()
    class Meta:
        model = NotesModel
        fields = '__all__'
        depth = 2
