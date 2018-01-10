from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from django.http import HttpResponse
from collections import defaultdict
import json
from rest_framework.decorators import detail_route
# Create your views here.

class Scolinfo:
    def general(request):
        data = []
        for ue in UEmodel.objects.all():
            ecs = []
            for ec in ECmodel.objects.filter(UE=ue):
                ecs.append({
                    'nom': ec.nom_ec,
                    'coef': ec.coef_ec,
                    'moyenne' : ec.moyenneEC,
                })
            data.append({
                'nom': ue.nom_ue,
                'coef': ue.coef_ue,
                'moyenne':ue.moyenneUE,
                'ECs':ecs,
            })
        return render(request, 'general.html', context={
            'data': data,
        })

class UEviewset(viewsets.ModelViewSet):
    queryset = UEmodel.objects.all()
    serializer_class = UEserializer

class ECviewset(viewsets.ModelViewSet):
    queryset = ECmodel.objects.all()
    serializer_class = ECserializer
    def get(self, request, pk):  #est-ce qu'on a le droit d'utiliser la PK d'un autre modèle
        queryset = ECviewset.objects.filter(UE=pk)
        serializer_class = ECserializer

class IEviewset(viewsets.ModelViewSet):
    queryset = IEmodel.objects.all()
    serializer_class = IEserializer
    @detail_route(methods=['get'])
    def get(self, request, ue, ec):
        queryset = IEviewset.objects.filter(UE=ue, EC=ec)
        serializer_class = IEserializer
