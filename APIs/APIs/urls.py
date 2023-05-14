from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.urls import re_path as url

from django.apps import apps
from rest_framework import routers

# /Volumes/dssDevelopment/djangular/APIs/APIs/views.py
from APIs.views import home
import observed.views as observedViews


from APIs import urls

router = routers.DefaultRouter()

urlpatterns = [

    path('admin_tools/',include('admin_tools.urls')),
    path('admin/', admin.site.urls),

    # path('observed/',include('observed.urls')),
    # path('observedClimatology/',include('observedClimatology.urls')),
    path('forecast/',include('forecast.urls')),
    # path('climatology/',include('climatology.urls')),
    # path('transport/',include('transport.urls')),
    path('', home, name='home'),

    # path('figureByParameter/<slug:slug>/', observedViews.figureByParameter),

    # path('template/',views.template_view),
    # path('scripts/',views.runScript,name='script')
]
