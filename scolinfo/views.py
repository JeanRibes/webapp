from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from django.http import HttpResponse
from collections import defaultdict
import json
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

class IEviewset(viewsets.ModelViewSet):
    queryset = IEmodel.objects.all()
    serializer_class = IEserializer