from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, detail_route
from rest_framework.views import APIView
from rest_framework import viewsets
from api.serializers import UserSerializer
from django.contrib.auth.models import User

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer
