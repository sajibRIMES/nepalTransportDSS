from django.urls import path,include
from rest_framework import routers


from transport import views

router = routers.DefaultRouter()

router.register(r'lged-road',views.lgedRoadViewSet,basename='upazila')

urlpatterns = [

    # path('',views.forecastHome),
    path('', include((router.urls,'transport'))),
    path('bd-roads', views.bdRoadViewSet.as_view({'get': 'list'})),
]