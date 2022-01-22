from django.urls import path

from . import views

app_name='places'

urlpatterns = [
    path('vet_clinics', views.get_clinics, name='clinics'),
    path('zooshops', views.get_shops, name='shops'),
    path('walking_areas', views.get_areas, name='areas'),
]