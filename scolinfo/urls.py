from django.conf.urls import url, include
from .views import *
from rest_framework_nested import routers
scolinfoRouter = routers.DefaultRouter()
scolinfoRouter.register(r'ue', UEviewset)
scolinfoRouter.register(r'ec', ECviewset)
scolinfoRouter.register(r'ie', IEviewset)
urlpatterns = [
    url(r'^', include(scolinfoRouter.urls)),
    url(r'^tout', Scolinfo.general),
    url(r'^ec/(?P<ue>[0-9]+)/$', ECviewset.get),
    url(r'^ie/(?P<ue>[0-9]+)/(?P<ec>[0-9]+)/$'),
]
        
