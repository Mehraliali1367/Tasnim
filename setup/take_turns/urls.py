from django.urls import path
from . import views

app_name = 'take_turns'
urlpatterns = [
    path('doctordifinit/', views.DoctorDifinit.as_view(), name='doctordifinit'),
    path('servicesdifinit/', views.ServicesDifinit.as_view(), name='servicesdifinit'),
    path('getdoctorapi/', views.GetDoctorApi.as_view(), name='getdoctorapi'),
    path('getdoctordateapi/', views.GetDoctorDateApi.as_view(), name='getdoctordateapi'),
    path('presencedoctor/', views.PresenceDoctor.as_view(), name='presencedoctor'),
    path('gethourvisit/', views.GetHourVisitApi.as_view(), name='gethourvisitapi'),
    path('visit/', views.Visit.as_view(), name='visit'),
]
