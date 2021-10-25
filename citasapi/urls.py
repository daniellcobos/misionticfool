
from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name= 'Dippi'
urlpatterns = [
    path('Doctor/all', views.DoctorList.as_view()),
    path('Doctor/save', views.DoctorList.as_view()),
    path('Doctor/update', views.DoctorList.as_view()),
    path('Doctor/<int:pk>', views.DoctorDetail.as_view()),
    path('Specialty/all', views.SpecialtyList.as_view()),
    path('Specialty/save', views.SpecialtyList.as_view()),
    path('Specialty/update', views.SpecialtyList.as_view()),
    path('Specialty/<int:pk>', views.SpecialtyDetail.as_view()),
    path('Client/all', views.ClientList.as_view()),
    path('Client/save', views.ClientList.as_view()),
    path('Client/update', views.ClientList.as_view()),
    path('Client/<int:pk>', views.ClientDetail.as_view()),
    ]