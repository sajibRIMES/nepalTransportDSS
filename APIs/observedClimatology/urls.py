from django.urls import path,include
from rest_framework import routers


from observedClimatology import views

router = routers.DefaultRouter()

router.register(r'tmax',views.tmaxViewSet,basename='tmax')

urlpatterns = [

    # path('',views.forecastHome),
    path('', include((router.urls,'observedClimatology'))),
    # path('bd-roads', views.bdRoadViewSet.as_view({'get': 'list'})),
]