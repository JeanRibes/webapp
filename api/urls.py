from django.conf.urls import url, include
from . import views
from rest_framework_nested import routers
from notes.views import moyenne

router = routers.DefaultRouter()
router.register(r'note', views.NotesViewSet)
router.register(r'matiere', views.MatiereViewSet)
urlpatterns = [
        url(r'^', include(router.urls)),
        url(r'^moyenne', moyenne),
        ]