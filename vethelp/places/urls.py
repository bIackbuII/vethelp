from django.urls import path

from . import views

app_name='places'

urlpatterns = [
    path('', views.show_info, name='info'),
    path('vet_clinics', views.get_clinics, name='clinics'),
    path('vet_clinics/<int:id>', views.get_profile, name='clinic'),
    path('vet_clinics/<int:clinic_id>/comment/', views.add_comment, name='add_comment'),
    path('walking_areas', views.get_areas, name='areas'),
]