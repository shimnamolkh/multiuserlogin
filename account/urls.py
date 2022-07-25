from django.urls import path
from .import  views

urlpatterns=[
     path('',views.login_view, name='login'),
     path('doctor_register/',views.doctor_register.as_view(), name='doctor_register'),
     path('patient_register/',views.patient_register.as_view(), name='patient_register'),
     path('doctor_home/',views.doctor_home, name='doctor_home'),
     path('patient_home/',views.patient_home, name='patient_home'),
     path('logout/',views.logout_view, name='logout'),
]