from django.urls import  path
from survey import views

urlpatterns = [
    path('getOption', views.GetOption.as_view()),
    path('vaccinationStatus', views.GetVaccinationStatus.as_view()),
    path('updateVaccinationStatus', views.UpdateVaccinationStatus.as_view()),

    ]