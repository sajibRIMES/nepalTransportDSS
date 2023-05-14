from django.urls import path,include
from rest_framework import routers


from forecast import views
# from forecast.views import daily_max_min,forecast_by_paremeter

router = routers.DefaultRouter()

# router.register(r'daily-forecast-by-parameter/(?P<id>\d+)',views.dailyForecastViewSet,basename='dailyForecast')
# router.register(r'daily-forecast',views.dailyForecastViewSet,basename='dailyForecast')
# router.register(r'hourly-forecast',views.hourlyForecastViewSet,basename='hourlyForecast')

urlpatterns = [

    # path('',views.forecastHome),
    path('', include((router.urls,'forecast'))),
    path('forecast-from-url/<slug:category>/<slug:parameter>/', views.forecastFromUrl),
    path('day-max-min/<slug:category>/<slug:parameter>/', views.dailyMaxMin),

    # path('daily-max-min',daily_max_min),

    # path('forecast-by-parameter/<slug:parameter_id>/',forecast_by_paremeter)
]