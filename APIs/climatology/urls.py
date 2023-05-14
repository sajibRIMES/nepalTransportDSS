from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from climatology import views

router = routers.DefaultRouter()
router.register(r'proverty',views.provertyViewSet,basename='proverty')
router.register(r'projection',views.climateViewSet,basename='projection')


urlpatterns = [
    path('', include((router.urls,'climatology')))
]