from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("province/aqi", views.get_aqi),
    path("provinces/average-aqi", views.get_average_aqi),
    path("add-data", views.add_air_data),
    path("add-year-data", views.add_year_data),
    #path("province/allPollutants", views.get_pollutants)
]
