from rest_framework import serializers
from .models import *

class UEserializer(serializers.ModelSerializer):
    moyenneUE = serializers.ReadOnlyField()
    class Meta:
        model =UEmodel
        fields = '__all__'
class ECserializer(serializers.ModelSerializer):
    moyenneEC = serializers.ReadOnlyField
    class Meta:
        model = ECmodel
        fields = '__all__'
        #depth = 2
class IEserializer(serializers.ModelSerializer):
    class Meta:
        model = IEmodel
        fields = '__all__'
      #  depth = 3