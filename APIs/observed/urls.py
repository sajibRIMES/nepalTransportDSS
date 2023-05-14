from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from observed import views


router = routers.DefaultRouter()

router.register(r'stations',views.StationViewSet,basename='station')
router.register(r'stationObserved',views.stationObservedViewSet,basename='stationobserved')
# router.register(r'threeHourlyObserved',views.stationObservedViewSet,basename='hourlyObserved')
# router.register(r'figures',views.figureViewSet,basename='figure')
# router.register(r'upload', views.uploadViewSet, basename="upload")

urlpatterns = [
    path('', include((router.urls,'observed'))),
    path('figureByParameter/<slug:category>/<slug:parameter>/', views.figureByParameter),
    # path('figureByParameter/<slug:parameter>/<slug:district>/<slug:other>/', views.figureByParameter),
    # path('', include((router.urls,'climatology'))),
]