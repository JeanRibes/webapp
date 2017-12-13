from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^moyenne', views.moyenne),
    url(r'^$', views.listeMatieres, name='liste'),
    url(r'^(?P<matiere>.+)$', views.listeNotes),
]
